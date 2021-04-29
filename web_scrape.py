#!/usr/bin/python3

# nist_scrape: given a cveID scrape the description and vulnerability rating from nist.gov

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

def set_data(cveID):
	nist_url = 'https://nvd.nist.gov/vuln/detail/' + cveID
	ibm_url = 'https://exchange.xforce.ibmcloud.com/vulnerabilities/' + cveID

	# open a connection, grab and download the web page
	nist_client = uReq(nist_url)
	nist_html = nist_client.read()	# raw HTML
	nist_client.close()

	ibm_client = uReq(ibm_url)
        ibm_html = ibm_client.read()  # raw HTML
        ibm_client.close()

	# if page not found do something
	# parse html	soup(raw html, how you want to parse it)
	global nist_soup
	nist_soup = soup(nist_html, 'html.parser')

	global ibm_soup
	ibm soup = soup(ibm_html, 'html.parser')


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

# Pre: set_data must be called
# return cost analysis
