#!/usr/bin/python3

# USAGE: write scan_results.csv

import csv
import re

scan_results = 'scan_results.csv'
results = open(scan_results, 'w')

raw = open('raw_results.txt', 'r')
port = -1
while True:
	line = raw.readline()
	# if line is empty the end of raw is reached
	if not line:
	 	break
	# if new_port(line)
		# port = regex
	if re.search(r' open ', line) != None:
		port = re.search(r'\d*', line).group(0)
	
	# print('get_ID' + '\t' + port + '\t' + 'description')
raw.close()
results.close()
