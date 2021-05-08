#!/usr/bin/python3

from nist_scrape import set_data, get_description, get_cvss 
import csv

vul_results_csv = 'vul_results.csv'
results = open(vul_results_csv, 'w')
headers = 'CVE ID\tport#\tcvss rating\tdescription\tlink\n'
results.write(headers)

with open('vul_scan_results.csv') as file:
	reader = csv.reader(file, delimiter='\t')
	for row in reader:
		if  set_data(row[0]):
			results.write(row[0] + '\t' + row[1] + '\t' +
		 	get_cvss() + '\t' + row[2] + '\t' + 
		 	'https://nvd.nist.gov/vuln/detail/'+row[0] + '\n')
results.close()
