#!/usr/bin/python3

from nist_scrape import set_data, get_description, get_cvss 
import csv

write_results = 'results.csv'
results = open(write_results, 'w')
headers = 'CVE name\tport#\tcvss\tseverity rating\tdescription\tlink\n'
results.write(headers)

with open('scan_results.csv') as file:
	reader = csv.reader(file, delimiter='\t')
	for row in reader:
		set_data(row[0])
		results.write(row[0] + '\t' + 'getPORT#' + '\t' +
			get_cvss() + '\t' + get_description() + '\t' + 
			'https://nvd.nist.gov/vuln/detail/'+row[0] + '\n')
results.close()