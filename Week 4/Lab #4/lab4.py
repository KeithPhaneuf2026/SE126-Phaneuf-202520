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
#firstName          list of first names
#lastName           list of last names
#age                list of employee ages
#screenName         screen names of employees
#houseAllegiance    list of groups or houses that employees are in
#email              emails of employees made during "for rec in file" process
#department         list of departments that employees are in according to their house allegiance
#phoneExtension     list of unique phone extensions of employees
#totalRecords       total number of employees
#totalResearch      total number of employees in Research and Development
#totalMarketing     total number of employees in Marketing
#totalResources     total number of employees in Human Resources
#totalAccounting    total number of employees in Accounting
#totalSales         total number of employees in Sales
#totalAuditing      total number of employees in Autiting
#answer             while y, sequential search is operating
#searchType         used to choose method of searching
#found              if value changes, value inputted by users was found
#searchFirst        used to search by first name, collects input from user and compares it to list
#searchPhone        used to search by phone extension, collects input from user and compares it to list
#searchLast         used to search by last name, collects input from user and compares it to list
#searchDepartment   used to search by department, collects input from user and compares it to list

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
#adding data to lists
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

#prints lists of employee records
for index in range(0, len(firstName)):
    print(f"{firstName[index]:8} {lastName[index]:10} {email[index]:30} {department[index]:27} {phoneExtension[index]:3}")
#formatting and printing all amounts of employees in different groups as well as total number of employees on file
print(f"-----------------------------------------------------------------------------------")
print(f"\nTotal number of employees on file:                      {totalRecords} Employees")
print(f"\nTotal number of employees in Research and Development:   {totalResearch} Employees")
print(f"\nTotal number of employees in Marketing:                  {totalMarketing} Employees")
print(f"\nTotal number of employees in Human Resources:            {totalResources} Employees")
print(f"\nTotal number of employees in Accounting:                 {totalAccounting} Employees")
print(f"\nTotal number of employees in Sales:                      {totalSales} Employees")
print(f"\nTotal number of employees in Auditing:                   {totalAuditing} Employees")
file = open("Week 4/Lab #4/westeros.csv", "w")

#writing to new file
for i in range(0, len(firstName)):
    file.write(f"{firstName[i]}, {lastName[i]}, {email[i]}, {department[i]}, {phoneExtension[i]}\n")
file.close()

#sequential search practice
print("\nWelcome to the Employee Search Program: ")
answer = input("\nWould you like to search for an employee? [Y/N]: ").lower()
while answer == "y":

    print("\t~Search Menu~")
    print("1: Search by FIRST name")         
    print("2: Search by PHONE EXTENSION")
    print("3: Search by LAST name")
    print("4: Search by DEPARTMENT")      
    print("5: EXIT")

    searchType = input("Enter your method of search (1-5): ")

    if searchType == "1":   #first name
        print("Searching by FIRST name")
        found = -1
        searchFirst = input("Enter the FIRST NAME of the employee you wish to search: ")
        for i in range(0, len(firstName)):
            if searchFirst.lower() == firstName[i].lower():
                found = i
        
        if found != -1:
            print(f"Your search for {searchFirst} was FOUND! Here is their data: ")
            print(f"{firstName[found]:8}  {lastName[found]:10}  {email[found]:30}  {department[found]:27}  {phoneExtension[found]:3}")
        else: 
            #NOT found
            print(f"Your search for {searchFirst} was NOT FOUND")
            print("Please check casing and/or spelling")
    elif searchType == "2":#phone
        print("Searching by PHONE EXTENSION")
        found = -1
        searchPhone = int(input("Enter the PHONE EXTENSION of the employee you wish to search: "))
        for i in range(0, len(phoneExtension)):
            if int(searchPhone) == int(phoneExtension[i]):
                found = i
        
        if found != -1:
            print(f"Your search for {searchPhone} was FOUND! Here is their data: ")
            print(f"{firstName[found]:8}  {lastName[found]:10}  {email[found]:30}  {department[found]:27}  {phoneExtension[found]:3}")
        else:
            print(f"Your search for {searchPhone} was NOT FOUND")
            print("Please check your input number")
    elif searchType == "3":#last name
        print("Searching by LAST name")
        found = []
        searchLast = input("Enter the LAST NAME of the employee you wish to search: ")
        for i in range(0, len(lastName)):
            if searchLast.lower() == lastName[i].lower():
                found.append(i)
        
        if not found:
            print(f"Your search for {searchLast} was NOT FOUND")
            print("Please check casing and/or spelling")
        else:
            print(f"Your search for {searchLast} was FOUND! Here is their data: ")
            for i in range (0, len(found)):
                print(f"{firstName[found[i]]:8}  {lastName[found[i]]:10}  {email[found[i]]:30}  {department[found[i]]:27}  {phoneExtension[found[i]]:3}")
    elif searchType == "4":#department
        print("Searching by DEPARTMENT")
        found = []
        searchDepartment = input("Enter the DEPARTMENT of the employee you wish to search: ")
        for i in range(0, len(department)):
            if searchDepartment.lower() == department[i].lower():
                found.append(i)
                
        if not found:
            print(f"Your search for {searchDepartment} was NOT FOUND")
            print("Please check casing and/or spelling")
        else:
            print(f"Your search for {searchDepartment} was FOUND! Here is a list of people in {searchDepartment}: ")
            for i in range (0, len(found)):
                print(f"{firstName[found[i]]:8}  {lastName[found[i]]:10}  {email[found[i]]:30}  {department[found[i]]:27}  {phoneExtension[found[i]]:3}")
    elif searchType == "5": #exit
        print("\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    
    #build a way out of the loop - answer should be able to change value! 
    if searchType == "1" or searchType == "2" or searchType == "3" or searchType == "4":
        #when search_type == "3" the user has chosen to exit, and if they did not provide a 1, 2, or 3 to search_type then they will automatically be brought back through the loop to see the menu again
        answer = input("Would you like to search again? [y/n]: ").lower()

#end of program message
print("\nThanks for using the search program. Goodbye!\n")