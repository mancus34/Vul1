#!/usr/bin/python3

# nist_scrape: given a cveID scrape the description and vulnerability rating from nist.gov

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

def set_data(cveID):
	nist_url = 'https://nvd.nist.gov/vuln/detail/' + cveID

	# open a connection, grab and download the web page
	nist_client = uReq(nist_url)
	nist_html = nist_client.read()	# raw HTML
	nist_client.close()

	# parse html	soup(raw html, how you want to parse it)
	global nist_soup
	nist_soup = soup(nist_html, 'html.parser')


# Pre: set_data must be called
# return description
def get_description():
	return nist_soup.find('p',{'data-testid':'vuln-description'}).text

# Pre: set_data must be called
# return cvss2 score screw the new scoring
def get_cvss():
	# grab cvss2 score
	s = str(nist_soup.find('div',{'id':'vulnCvssPanel'})\
		.find('div',{'id':'Vuln2CvssPanel'})\
		.find('span',{'class':'severityDetail'}).a.text)
	return str(re.search(r'\d*\.\d', s).group(0))
