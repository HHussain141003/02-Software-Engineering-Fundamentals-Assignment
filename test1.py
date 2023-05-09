# Name:                 Test1.py
# Created on:           21/03/2023

import csv
from prettytable import from_csv

# Display CSV Table at the start of the application.
with open("Data.csv") as fp:
    varObjTable = from_csv(fp)
print(varObjTable)


def addRecord():
    with open('Data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        # determine the next issue number by finding the highest issue number in the existing data
        with open('Data.csv', mode='r') as existing_file:
            reader = csv.DictReader(existing_file)
            issue_numbers = [int(row['IssueNo.']) for row in reader]
            next_issue_number = max(issue_numbers) + 1

        # prompt the user for the new issue data
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        telephone = input("Enter your telephone number: ")
        email = input("Enter your email: ")
        severity = input("Enter the severity (Low, Medium, or High): ")
        issue_type = input("Enter the issue type: ")
        comments = input("Enter any comments: ")
        days_affected = input("Enter the number of days affected: ")
        solved = input("Is the issue solved? (Yes or No): ")

        # write the new issue data to the CSV file
        writer.writerow([next_issue_number, name, surname, telephone, email, severity, issue_type, comments, days_affected, solved])

    print("Issue added successfully!")
# Let the user decide whether they want to Create a new record, Edit an existing record or Delete an existing record.
varUserAction = ""

while varUserAction != "Exit":
    varUserAction = input("Please type in the action you want to carry out (New/Edit/Delete/Exit): ")
# ----------------------------------------------------------------------------------------------------------------------
    if varUserAction == "New":
        addRecord()
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