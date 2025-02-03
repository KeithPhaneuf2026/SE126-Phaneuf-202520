#Keith Phaneuf
#SE126.04
#Lab 4
#1-29-2025 [W4D2]

#PROGRAM PROMPT:
'''
PART 1
Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension.

When you are complete, display the following data for each employee (first name, last name, department, email, and phone extension) to the user. 

PART 2
Once you have completed populating all eight parallel lists and displaying the five required back to the user (and in the same Python file), create and write the following data for each employee to a file named westeros.csv: first name, last name, email, department, and phone extension. Each employees data should be on its own record (row) within the newly created file. You will most likely end up with an extra empty line at the end of the file (this is okay for this lab as we will not be reprocessing the data found in this new file). 
Once the file is ready, close it and alert the user via a displayed message. Also tell them how many employees are in the file, and the total count of employees for each department.
'''

#Variable Dictionary

#Functions

#imports
import csv
import random

#record counting variables
totalRecords = 0

#lists
firstName = []
lastName = []
age = []
screenName = []
houseAllegiance = []
email = []
department = []
phoneExtension = []

#connected
totalRecords = 0
totalResearch = 0
totalMarketing = 0
totalResources = 0
totalAccounting = 0
totalSales = 0
totalAuditing = 0
print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':27} {'EXT':3}")
print(f"-----------------------------------------------------------------------------------")
with open ("Week 4/Lab #4/got_emails.csv") as csvfile:

    file = csv.reader(csvfile)
    for rec in file: 
        totalRecords += 1
        firstName.append(rec[0])
        lastName.append(rec[1])
        age.append(int(rec[2]))
        screenName.append(rec[3])
        houseAllegiance.append(rec[4])
        email.append(rec[3] + "@westeros.net")
        if rec[4] == "House Stark":
            department.append("Research and Development")
            totalResearch += 1
            phoneExtension.append(random.randint(100, 199))
        elif rec[4] == "House Targaryen":
            department.append("Marketing")
            totalMarketing += 1
            phoneExtension.append(random.randint(200, 299))
        elif rec[4] == "House Tully":
            department.append("Human Resources")
            totalResources += 1
            phoneExtension.append(random.randint(300, 399))
        elif rec[4] == "House Lannister":
            department.append("Accounting")
            totalAccounting += 1
            phoneExtension.append(random.randint(400, 499))
        elif rec[4] == "House Baratheon":
            department.append("Sales")
            totalSales += 1
            phoneExtension.append(random.randint(500, 599))
        elif rec[4] == "The Night's Watch":
            department.append("Auditing")
            totalAuditing += 1
            phoneExtension.append(random.randint(600, 699))
        else:
            department.append("----------")
            phoneExtension.append("------")

for index in range(0, len(firstName)):
    print(f"{firstName[index]:8} {lastName[index]:10} {email[index]:30} {department[index]:27} {phoneExtension[index]:3}")
print(f"-----------------------------------------------------------------------------------")
print(f"\nTotal number of employees on file: {totalRecords}")
print(f"\nTotal number of employees in Research and Development: {totalResearch}")
print(f"\nTotal number of employees in Marketing: {totalMarketing}")
print(f"\nTotal number of employees in Human Resources: {totalResources}")
print(f"\nTotal number of employees in Accounting: {totalAccounting}")
print(f"\nTotal number of employees in Sales: {totalSales}")
print(f"\nTotal number of employees in Auditing: {totalAuditing}")
file = open("Week 4/Lab #4/westeros.csv", "w")

for i in range(0, len(firstName)):
    file.write(f"{firstName[i]}, {lastName[i]}, {email[i]}, {department[i]}, {phoneExtension[i]}\n")
file.close()