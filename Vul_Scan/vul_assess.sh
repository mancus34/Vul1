#!/bin/sh

echo -n "Enter the IP address you would like to scan: "
read address

echo "Starting Vulnerability Scan..."
nmap --script vulscan -sV ${address} > raw_results.txt
echo "Reading results..."
./modify_raw_results.py
echo "Interpreting results..."
./write_csv_file.py
echo "Scan finished. You can view the results by openinWEBSITE"
