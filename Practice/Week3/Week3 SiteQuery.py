from unittest import result
from urllib import response
import requests
import time
import csv
import re

response = requests.get('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
results = response.json()["result"]["results"]

CSVData=[]
    
def getFirstFile(s):
    for items in results:

        if time.strptime(items["xpostDate"], "%Y/%m/%d")[0] >= 2015:
            file = items["file"].split("https://")[1]
            data = (items["stitle"], items["address"][5:8], items["longitude"], items["latitude"], "https://" + file)
            dataString = ",".join(data)
            CSVData.append(dataString)
           

getFirstFile(results)
CSVData = "\n".join(CSVData)
with open("SitesQueryResults.csv", mode="w", encoding="utf-8") as file:
    file.write(CSVData)