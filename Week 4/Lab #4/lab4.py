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
            phoneExtension.append(random.choice([100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129]))
        elif rec[4] == "House Targaryen":
            department.append("Marketing")
            totalMarketing += 1
            phoneExtension.append(random.choice([200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229]))
        elif rec[4] == "House Tully":
            department.append("Human Resources")
            totalResources += 1
            phoneExtension.append(random.choice([300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329]))
        elif rec[4] == "House Lannister":
            department.append("Accounting")
            totalAccounting += 1
            phoneExtension.append(random.choice([400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429]))
        elif rec[4] == "House Baratheon":
            department.append("Sales")
            totalSales += 1
            phoneExtension.append(random.choice([500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529]))
        elif rec[4] == "The Night's Watch":
            department.append("Auditing")
            totalAuditing += 1
            phoneExtension.append(random.choice([600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629]))
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