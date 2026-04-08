import os
import csv

km_list = []
price_list = []

with open("data.csv", "r") as dataFile:
    load_data = csv.DictReader(dataFile)
    for row in load_data:
        km_list.append (float(row["km"]))
        price_list.append(float(row["price"]))
