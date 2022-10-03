from unittest import result
from urllib import response
import requests
import time
import csv
import re

response = requests.get('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
# print(response.status_code)
# print(response.json())
results = response.json()["result"]["results"]

Dates = "2015/01/01"
CSVData=[]
delimeter ="\n"

for items in results:

    if time.strptime(items["xpostDate"], "%Y/%m/%d")[0] >= 2015:
            file = items["file"].split("https://")[1]
            data = (items["stitle"], items["address"][5:8], items["longitude"], items["latitude"], file)
            dataString = ",".join(data)
            CSVData.append(dataString)

# def regexFind (s):
#     result = re.findall(r"(http|https)://", s)
#     print(result)



CSVData = "\n".join(CSVData)
print("===")
print(type(items["file"]))
print(CSVData)

with open("QueryResults.csv", mode="w", encoding="utf-8") as file:
    file.write(CSVData)