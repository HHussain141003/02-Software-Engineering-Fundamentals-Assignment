# Name:                 Test1.py
# Created on:           21/03/2023

import csv
import os
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
        while True:
            Name = input("Enter your name: ")
            if any(char.isdigit() for char in Name):
                print("Please enter a valid name!")
            else:
                break
        while True:
            Surname = input("Enter your surname: ")
            if any(char.isdigit() for char in Name):
                print("Please enter a valid surname!")
            else:
                break
        while True:
            Telephone = input("Enter your telephone number: ")
            if not Telephone.isdigit() or len(Telephone) != 11:
                print("Please enter a valid number!")
            else:
                break
        while True:
            Email = input("Enter your email: ")
            if '@' not in Email:
                print("Please enter a valid Email!")
            else:
                break
        while True:
            Severity = input("Enter the severity (Low, Medium, or High): ")
            if Severity not in ['Low', 'Medium', 'High']:
                print("Please choose a suitable severity from Low, Medium or High!")
            else:
                break
        Type = input("Enter the issue type: ")
        Comments = input("Enter any comments: ")
        while True:
            Days_Affected = input("Enter the number of days affected: ")
            if not Days_Affected.isdigit() or int(Days_Affected) < 0 or int(Days_Affected) > 100:
                print("Please enter a valid Number!")
            else:
                break
        while True:
            Solved = input("Is the issue solved? (Yes or No): ")
            if Solved not in ['Yes', 'No']:
                print("Please enter a suitable value Yes/No")
            else:
                break

        file.seek(0, 2)  # move the pointer to the end of the file
        writer.writerow([IssueNo, Name, Surname, Telephone, Email, Severity, Type, Comments, Days_Affected, Solved])

    print("Issue added successfully!")

# Delete record function
def delete_record():
    Issue_No = input("Enter the IssueNo to delete: ")
    temp_file = "temp.csv"

    with open('Data.csv', mode='r') as file, open(temp_file, mode='w', newline='') as temp:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(temp, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            if row['IssueNo'] != Issue_No:
                writer.writerow(row)

    os.remove('Data.csv')
    os.rename(temp_file, 'Data.csv')
    print("Record deleted successfully!")

# Let the user decide whether they want to Create a new record, Edit an existing record or Delete an existing record.
user_action = ""

table()
while user_action != "X":
    print("Please choose the action you want to carry out from the following options:")
    print("N - New record")
    print("E - Edit record")
    print("D - Delete record")
    print("X - Exit application")
    print("")
    user_action = input("Action: ")
# ----------------------------------------------------------------------------------------------------------------------
    if user_action == "N":
        add_record()
        print("New Record added successfully!")
        table()
# ----------------------------------------------------------------------------------------------------------------------
    elif user_action == "E":
        print("Test: Edit")
# ----------------------------------------------------------------------------------------------------------------------
    elif user_action == "D":
        delete_record()
        table()
# ----------------------------------------------------------------------------------------------------------------------
    elif user_action == "X":
        print("Exited the app successfully")
# ----------------------------------------------------------------------------------------------------------------------
    else:
        print("Error, please enter a correct value")
