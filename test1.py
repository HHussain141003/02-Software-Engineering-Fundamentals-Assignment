# Name:                 Test1.py
# Created on:           21/03/2023
import csv
from prettytable import from_csv

with open("Data.csv") as fp:
    varObjTable = from_csv(fp)
print(varObjTable)

