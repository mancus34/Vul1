#!/bin/sh

echo "Usage: scan a device for Common Vulnerabilities and Exposures (CVE)." 
echo -n "Enter the IP address you would like to scan: "
read address

echo "Starting Vulnerability Scan..."
nmap --script vulscan -sV ${address} > vul_raw_results.txt
echo "Filtering results..."
./vul_modify_raw_results.py
echo "Assessing results..."
./vul_write_csv_file.py

awk 'NR == 1; NR > 1 {print $0 | "sort -nr -k3"}' vul_results.csv > tmp.csv
mv tmp.csv vul_results.csv
cp vul_results.csv vatGUI
echo "Assessment Complete. You can view the results by opening the User Interface."
