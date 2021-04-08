#!/usr/bin/python3

# nist_scrape: given a cveID scrape the description and vulnerability rating from nist.gov

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

def set_data(cveID):
	my_url = 'https://nvd.nist.gov/vuln/detail/' + cveID
	print(my_url)
	# open a connection, grab the page
	# download the webpage
	# uClient = uReq(my_url)
	# raw html
# 	page_html = uClient.read()
# 	uClient.close()

	# if page not found do something
	# parse html	soup(raw html, how you want to parse it)	the name soup is comminly used
# 	global page_soup
# 	page_soup = soup(page_html, 'html.parser')


# Pre: set_data must be called
# return description
def get_description():
	return page_soup.find('p',{'data-testid':'vuln-description'}).text

# Pre: set_data must be called
# return cvss2 score screw the new scoring
def get_cvss():
	# grab cvss2 score
	str = str(page_soup.find('div',{'id':'vulnCvssPanel'})\
		.find('div',{'id':'Vuln2CvssPanel'})\
		.find('span',{'class':'severityDetail'}).a.text)
	return re.search(r'[0-9]', str)

#return how to fix vulnerability
