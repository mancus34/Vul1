#!/bin/sh
# push the entire directory to github mancus34/Vul_Scan
# USAGE: provide commit name

# echo -n "Enter commit name: 
# read name

# git init
# git add -a
# git commit -m ${description}"
# git commit -M main
git remote add origin https://github.com/mancus34/Vul_Scan.git
# git push -u origin main
git branch -M main
git push -u origin main
echo "Finished... see changes on github.com"
