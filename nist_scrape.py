#!/usr/bin/python3

# nist_scrape: given a cveID scrape the description and vulnerability rating from nist.gov

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def set_data(cveID):
	my_url = 'https://nvd.nist.gov/vuln/detail/' + cveID

	# open a connection, grab the page
	uClient = uReq(my_url)      # download the webpage
	page_html = uClient.read()  # raw html
	uClient.close()

	# if page not found do something
	# parse html	soup(raw html, how you want to parse it)	the name soup is comminly used
	global page_soup
	page_soup = soup(page_html, 'html.parser')


# Pre: set_data must be called
# return description
def get_description():
	return page_soup.find('p',{'data-testid':'vuln-description'}).text

# Pre: set_data must be called
# return cvss score
def get_cvss():
	if page_soup.find('div',{'id':'vulnCvssPanel'})\
		.find('div',{'id':'Vuln3CvssPanel'})\
		.find('span',{'class':'severityDetail'}).a.text != 'N/A':

		# grab cvss3 score
		return str(page_soup.find('div',{'id':'vulnCvssPanel'})\
			.find('div',{'id':'Vuln3CvssPanel'})\
			.find('span',{'class':'severityDetail'}).a.text)
	else:
		# grab cvss2 score
		return str(page_soup.find('div',{'id':'vulnCvssPanel'})\
			.find('div',{'id':'Vuln2CvssPanel'})\
			.find('span',{'class':'severityDetail'}).a.text)
