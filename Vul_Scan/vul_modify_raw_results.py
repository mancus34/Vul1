#!/usr/bin/python3

# USAGE: write scan_results.csv

import csv
import re

vul_scan_results = 'vul_scan_results.csv'
results = open(vul_scan_results, 'w')

raw = open('vul_raw_results.txt', 'r')
port = -1
while True:
	line = raw.readline()
	# if line is empty the end of raw is reached
	if not line:
	 	break
	# port change
	if re.search(r' open ', line) != None:
		port = str(re.search(r'\d*', line).group(0))
	# if its a CVE vulnerability
	if (re.search(r'\[CVE-.*', line)) != None:
		cve_id = str(re.search(r'CVE-\d*-\d*', line).group(0))
		description = str(line[18:])
		results.write(cve_id + '\t' + port + '\t' + description)
raw.close()
results.close()
