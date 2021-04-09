#!/bin/sh
# push the entire directory to github mancus34/Vul_Scan
# USAGE: provide commit name

echo -n "Enter commit brief description: "
read description

git init
git add -A
git commit -m "${description}"
git commit -M main
git remote add origin https://github.com/mancus34/name.git
git push -u origin main

echo "Finished... see changes on github.com"
