#!/bin/sh

echo "Reminder: Only Super Users can scan for IP connected devices\n"
sudo arp-scan -l tail -n +3 | head -n -3 > ip_raw_results.csv
./write_ip_csv_file.py
