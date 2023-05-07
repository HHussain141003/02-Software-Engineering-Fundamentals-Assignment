# Name:                 Test1.py
# Created on:           21/03/2023
import csv
from prettytable import from_csv

# Display CSV Table at the start of the application.
with open("Data.csv") as fp:
    varObjTable = from_csv(fp)
print(varObjTable)

# Let the user decide whether they want to Create a new record, Edit an existing record or Delete an existing record.
varUserAction = input("Please type in the action you want to carry out (New/Edit/Delete): ")
print("Input output (Test Ignore): ", varUserAction)

if varUserAction == "New":
    print("Test: New")
elif varUserAction == "Edit":
    print("Test: Edit")
elif varUserAction == "Delete":
    print("Test: Delete")
else:
    print("Error, please enter a correct value")