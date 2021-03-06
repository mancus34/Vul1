#!/usr/bin/python3

# nist_scrape: given a cveID scrape the description and vulnerability rating from nist.gov

from urllib.request import urlopen as uReq
from urllib.error import HTTPError
from bs4 import BeautifulSoup as soup
import re

def set_data(cveID):
	nist_url = 'https://nvd.nist.gov/vuln/detail/' + cveID

	try:
		# open a connection, grab and download the web page
		nist_client = uReq(nist_url)
		nist_html = nist_client.read()	# raw HTML
		nist_client.close()

		# parse html	soup(raw html, how you want to parse it)
		global nist_soup
		nist_soup = soup(nist_html, 'html.parser')

		return True

	except HTTPError:
		return False

# Pre: set_data must be called
# return description
def get_description():
	try:
		s = nist_soup.find('p',{'data-testid':'vuln-description'})

		if s is None:
			return 'description not found'

		return str(s.text)
	except NameError:
		return 'invalid CVE'

# Pre: set_data must be called
# return cvss2 score screw the new scoring
def get_cvss():
	try:
		# grab cvss2 score
		s = nist_soup.find('div',{'id':'vulnCvssPanel'})

		if s is None:
			return 'cvss not found'

		s = s.find('div',{'id':'Vuln2CvssPanel'})\
		.find('span',{'class':'severityDetail'}).a.text
		return str(re.search(r'\d*\.\d', s).group(0))

	except NameError:
		return 'invalid CVE'
