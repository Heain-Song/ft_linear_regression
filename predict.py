import os
import csv

def estimatedPrice (theta0, theta1, kilometer):
    return theta0 + (theta1 * kilometer)

if os.path.exists("thetas.csv"):
    with open("thetas.csv", "r") as thetasFile:
        reader = csv.DictReader(thetasFile)
        for row in reader:
            theta0 = float(row["theta0"])
            theta1 = float(row["theta1"])
else:
    theta0 = 0
    theta1 = 0

kilometer = float(input("Enter km: "))
print(estimatedPrice(theta0, theta1, kilometer))
