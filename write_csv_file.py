#!/usr/bin/python3

from nist_scrape import set_data, get_description, get_cvss 
import csv

results_csv = 'results.csv'
results = open(results_csv, 'w')
headers = 'CVE name\tport#\tcvss\tseverity rating\tdescription\tlink\n'
results.write(headers)

with open('scan_results.csv') as file:
	reader = csv.reader(file, delimiter='\t')
	for row in reader:
		 set_data(row[0])
		 results.write(row[0] + '\t' + row[1] + '\t' +
		 	get_cvss() + '\t' + row[2] + '\t' + 
		 	'https://nvd.nist.gov/vuln/detail/'+row[0] + '\n')
results.close()
