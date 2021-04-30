#!/usr/bin/python3

import csv

ip_results = 'ip_results.csv'
results = open(ip_results, 'w')
headers = 'IP Address\tMAC Address\tDevice\n'
results.write(headers)

with open('ip_raw_results.csv') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
                 results.write(row[0] + '\t' + row[1] + '\t' + row[2] + '\n')
results.close()

