# Name:                 Test1.py
# Created on:           21/03/2023

import csv
from prettytable import from_csv

# Display CSV Table at the start of the application.
with open("Data.csv") as fp:
    varObjTable = from_csv(fp)
print(varObjTable)

# Let the user decide whether they want to Create a new record, Edit an existing record or Delete an existing record.
varUserAction = ""

while varUserAction != "Exit":
    varUserAction = input("Please type in the action you want to carry out (New/Edit/Delete/Exit): ")
# ----------------------------------------------------------------------------------------------------------------------
    if varUserAction == "New":
        with open('Data.csv', mode='a') as existing_file:
            def add_row():

            issue_no = input('Enter IssueNo.: ')
            name = input('Enter Name: ')
            surname = input('Enter Surname: ')
            telephone = input('Enter Telephone: ')
            email = input('Enter Email: ')
            severity = input('Enter Severity: ')
            it_type = input('Enter Type: ')
            comments = input('Enter Comments: ')
            days_affected = input('Enter Days_Affected: ')
            solved = input('Enter Solved?: ')
        print("Test: New")
# ----------------------------------------------------------------------------------------------------------------------
    elif varUserAction == "Edit":
        print("Test: Edit")
# ----------------------------------------------------------------------------------------------------------------------
    elif varUserAction == "Delete":
        print("Test: Delete")
# ----------------------------------------------------------------------------------------------------------------------
    elif varUserAction == "Exit":
        print("Test: Exit")
# ----------------------------------------------------------------------------------------------------------------------
    else:
        print("Error, please enter a correct value")