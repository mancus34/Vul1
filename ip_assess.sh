#!/bin/sh

echo "Usage: create a list of IP connected devices."
echo "Reminder: Only Super Users can scan for IP connected devices."
echo "Once you enter your password, the scan will start.\n"
sudo arp-scan -l | tail -n +3 | head -n -3 > ip_raw_results.csv
./ip_write_csv_file.py
cp ip_results.csv vatGUI
echo "Assessment Complete. You can viw the reuslts by opening the User Interface."
