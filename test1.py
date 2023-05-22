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

        file.seek(0, 2)  # Move the pointer to the end of the file
        writer.writerow([IssueNo, Name, Surname, Telephone, Email, Severity, Type, Comments, Days_Affected, Solved])

    print("New record added successfully!")

# Delete record function
def delete_record():
    Issue_No = input("Enter the Issue Number you want to delete: ")
    confirmation = ""
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
        
# Edit record function
def edit_record():

    issue_no = input("Enter the issue number to edit: ")

    with open('Data.csv', mode='r', newline='') as existing_file:
        reader = csv.DictReader(existing_file)
        rows = [row for row in reader]

    # Find IssueNo Index
    row_index = None
    for i, row in enumerate(rows):
        if row['IssueNo'] == issue_no:
            row_index = i
            break

    # If the issue number was not found, print an error message and return
    if row_index is None:
        print(f"Issue number {issue_no} not found")
        return

    # Get the existing row values
    existing_row = rows[row_index]

    # Display the existing values and prompt for new values
    print("Existing information:")
    for key, value in existing_row.items():
        print(f"{key}: {value}")

    print("\nEnter new information (leave blank to keep existing value):")
    name = input("Name: ")
    if not name:
        name = existing_row['Name']

    surname = input("Surname: ")
    if not surname:
        surname = existing_row['Surname']

    telephone = input("Telephone: ")
    if not telephone:
        telephone = existing_row['Telephone']

    email = input("Email: ")
    if not email:
        email = existing_row['Email']

    severity = input("Severity (Low, Medium, High): ")
    if not severity:
        severity = existing_row['Severity']

    issue_type = input("Issue type: ")
    if not issue_type:
        issue_type = existing_row['Type']

    comments = input("Comments: ")
    if not comments:
        comments = existing_row['Comments']

    days_affected = input("Days affected: ")
    if not days_affected:
        days_affected = existing_row['Days_Affected']

    solved = input("Solved? (Yes or No): ")
    if not solved:
        solved = existing_row['Solved']

    # Update the row values
    rows[row_index]['Name'] = name
    rows[row_index]['Surname'] = surname
    rows[row_index]['Telephone'] = telephone
    rows[row_index]['Email'] = email
    rows[row_index]['Severity'] = severity
    rows[row_index]['Type'] = issue_type
    rows[row_index]['Comments'] = comments
    rows[row_index]['Days_Affected'] = days_affected
    rows[row_index]['Solved'] = solved

    # Write the updated rows back to the file
    with open('Data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IssueNo', 'Name', 'Surname', 'Telephone', 'Email', 'Severity', 'Type', 'Comments', 'Days_Affected', 'Solved'])
        for row in rows:
            writer.writerow([row['IssueNo'], row['Name'], row['Surname'], row['Telephone'], row['Email'], row['Severity'], row['Type'], row['Comments'], row['Days_Affected'], row['Solved']])

    print("Record edited successfully!")

# User Menu
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

    if user_action == "N":
        add_record()
        table()
    elif user_action == "E":
        edit_record()
        table()
    elif user_action == "D":
        delete_record()
        table()
    elif user_action == "X":
        print("Exited the app successfully")
    else:
        print("Error, please enter a correct value")
