# Name:                 Test1.py
# Created on:           21/03/2023

import csv
from prettytable import from_csv
from prettytable import PrettyTable

# Display CSV Table at the start of the application.
def table():
    with open("Data.csv") as fp:
        table = from_csv(fp)
    print(table)

# Add New record function
def add_record():
    with open('Data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        # Automatically determine the primary key (IssueNo + 1)
        with open('Data.csv', mode='r') as existing_file:
            reader = csv.DictReader(existing_file)
            IssueNo = [int(row['IssueNo']) for row in reader]
            IssueNo = max(IssueNo) + 1
        # Validation for the necessary fields.
        Name = input("Enter your name: ")
        Surname = input("Enter your surname: ")
        Telephone = input("Enter your telephone number: ")
        Email = input("Enter your email: ")
        Severity = input("Enter the severity (Low, Medium, or High): ")
        Type = input("Enter the issue type: ")
        Comments = input("Enter any comments: ")
        Days_Affected = input("Enter the number of days affected: ")
        Solved = input("Is the issue solved? (Yes or No): ")

        file.seek(0, 2)  # move the pointer to the end of the file
        writer.writerow([IssueNo, Name, Surname, Telephone, Email, Severity, Type, Comments, Days_Affected, Solved])

    print("Issue added successfully!")



# Let the user decide whether they want to Create a new record, Edit an existing record or Delete an existing record.
user_action = ""

table()
while user_action != "Exit":
    user_action = input("Please type in the action you want to carry out (New/Edit/Delete/Exit): ")
# ----------------------------------------------------------------------------------------------------------------------
    if user_action == "New":
        add_record()
        print("New Record added successfully!")
        table()
# ----------------------------------------------------------------------------------------------------------------------
    elif user_action == "Edit":
        print("Test: Edit")
# ----------------------------------------------------------------------------------------------------------------------
    elif user_action == "Delete":
        print("Test: Delete")
# ----------------------------------------------------------------------------------------------------------------------
    elif user_action == "Exit":
        print("Exited the app successfully")
# ----------------------------------------------------------------------------------------------------------------------
    else:
        print("Error, please enter a correct value")