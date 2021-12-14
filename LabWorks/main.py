import requests
from bs4 import BeautifulSoup
import csv

# Get the page & Put Soup on it
page = requests.get("https://cve.mitre.org/data/refs/refmap/source-MS.html").text
soup = BeautifulSoup(page , "lxml")


# Extracting Ms and CVE from the page
MS_CVE = soup.find_all("table" , cellpadding="2")[1].text

arr = MS_CVE.split("\n")

# clean the array
for i in arr:
    if i == '':
        arr.remove(i)
    else:
        pass


# name of cols
cols = ["MS Number" , "CVE Number"]

writeout = []
for i , item in enumerate(arr):
    if item.startswith("MS:MS15") or item.startswith("MS:MS16"):
        temp = []
        temp.append(item)
        temp.append(arr[i+1])

        writeout.append(temp)

print(writeout)
with open("Data.csv" , "w" , newline="\n") as f:
    writer = csv.writer(f)
    writer.writerow(cols)
    for i in writeout:
        writer.writerow(i)






