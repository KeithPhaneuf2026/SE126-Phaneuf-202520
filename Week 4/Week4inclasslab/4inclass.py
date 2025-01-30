#Keith Phaneuf
#SE126.04
#in class lab
#1-27-2025 [W4D1]

#PROGRAM PROMPT:
'''Part 1

Done: Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.

Original File Headers

FIELD0             FIELD1            FIELD2       FIELD3        FIELD4     

Firstname          Lastname        Test1         Test2             Test3

 

Part 2

Done: Next, reprocess the lists to find each student's current average score, letter grade equivalent, and the class average.  While processing in the for loop, store each student's average into a new list called 'num_avg' and their letter grade into a list called 'let_avg'. Then, print each student's full information, record by record including average score and average letter equivalent.  After this print of the original file data from the lists, print to the console the total number of student's in the class along with the class numeric average.  

 

Processed Parallel List Headers

FIELD0             FIELD1            FIELD2       FIELD3        FIELD4     FIELD5      FIELD6

firstName          lastName        test1         test2             test3       num_avg   let_avg

 

Part 3

After your final display using the 1D parallel lists, create a sequential search program which allows the user to repeatedly utilize the following menu of search types. When a searched for item is found, display all student data to the console. When a search is compete and no matching data is found, alert the user. Search options 1 and 2 should only show one found student, where search option 3 should show a potential of multiple students.

 

Search Menu

1. Search by LAST name 

2. Search by FIRST name

3. Search by LETTER GRADE

4. Exit'''

#Variable Dictionary
#firstName          list of first names
#lastName           list of last names
#test1              list of test1 grades
#test2              list of test2 grades
#test3              list of test3 grades
#num                number that reflects grade of test in letter() function
#letterGrade        determines letter grade in letter() function
#total_records      counts total number of records/students
#num_avg            determines average grade
#let_avg            determines letter grade for student
#total_avg          adds up all student averages to find class average
#class_avg          class average grade
#answer             allows while loop to be used by user command
#searchType         a numeric value used to run different sequential searches
#found              if value changes, value inputted by users was found
#searchLast         input value for last name search
#searchFirst        input value for first name search
#searchLetter       input value for letter grade

#Functions
def letter(num):
    if num >= 90:
        letterGrade = "A"
    elif num >= 80:
        letterGrade = "B"
    elif num >= 70:
        letterGrade = "C"
    elif num >= 60:
        letterGrade = "D"
    elif num <= 60:
        letterGrade = "F"
    else:
        letterGrade = "ERROR"
    
    return letterGrade
#imports
import csv

#record counting variable
total_records = 0

#lists
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

#connected
print(f"{'FIRST':10}  {'LAST':10}   {'T1':3}  {'T2':3}  {'T3':3} {'num_avg'}  {"let_avg"}")
print("-----------------------------------------------------------------------------")
with open("Week 4\Week4inclasslab\class_grades-2.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        #counts records
        total_records += 1
        #store data from current record to corresponding lists (each field on its own)
        #.append --> data dispersed across lists, connected by the same index
        
        #parallel lists --> data dispersed across lists, connected by the same index
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

num_avg = []
let_avg = []

for i in range(0, len(test1)):

    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)
    let_avg.append(letter(a))

for index in range(0, len(firstName)):
    #for every item, index will start at 0 and run up to (not including) the length (# of items)
    print(f"{firstName[index]:10}  {lastName[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3}  {num_avg[index]:.2f}    {let_avg[index]}")
print("-----------------------------------------------------------------------------")

#finds the entire class average using a for loop to add each student's avg to the class total
total_avg = 0
for i in range(0, len(num_avg)):
    total_avg += num_avg[i]

class_avg = total_avg / len(num_avg)

print(f"\nTOTAL RECORDS: {total_records}\nCURRENT CLASS AVERAGE: {class_avg:.2f}")

#sequential search
print("\nWelcome to Student Search")
answer = input("Would you like to search for a student's records? (Y/N)").lower()
while answer == "y":

    print("\t~Search Menu~")
    print("1. Search by LAST name")         #one search value found
    print("2. Search by FIRST name")
    print("3. Search by LETTER grade")      #multiple search values found
    print("4. EXIT")

    searchType = input("Enter your method of search (1-4)")

    if searchType == "1":   #last name
        print("Searching by LAST name")
        found = -1
        searchLast = input("Enter the LAST name of the person you wish to search:")
        for i in range(0, len(lastName)):
            if searchLast.lower() == lastName[i].lower():
                found = i
        
        if found != -1:
            print(f"Your search for {searchLast} was FOUND! Here is their data: ")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}  {let_avg[found]}")
        else: 
            #NOT found
            print(f"Your search for {searchLast} was NOT FOUND")
            print("Please check casing and/or spelling")
    elif searchType == "2": #first name
        print("Searching by FIRST name")
        found = -1
        searchFirst = input("Enter the FIRST name of the person you wish to search:")
        for i in range(0, len(firstName)):
            if searchFirst.lower() == firstName[i].lower():
                found = i
        
        if found != -1:
            print(f"Your search for {searchFirst} was FOUND! Here is their data: ")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}  {let_avg[found]}")
        else: 
            #NOT found
            print(f"Your search for {searchFirst} was NOT FOUND")
            print("Please check casing and/or spelling")
    elif searchType == "3": #letter grade
        print("Searching by LETTER grade")
        found = []
        searchLetter = input("Enter the LETTER grade of the student/s you wish to search:")
        for i in range(0, len(let_avg)):
            if searchLetter.upper() == let_avg[i]:
                found.append(i)
                print(f"Found a {searchLetter} grade in INDEX {i}")
        if not found:
            print(f"Your search for {searchLast} was NOT FOUND")
            print("Please check casing and/or spelling")
        else:
            print(f"Found a {searchLetter} grade in INDEX {i}")
            for i in range(0, len(found)):
                print(f"{firstName[found[i]]:10}  {lastName[found[i]]:10}  {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3}  {num_avg[found[i]]:6.1f}  {let_avg[found[i]]}")
    elif searchType == "4": #exit
        print("\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    
    #build a way out of the loop - answer should be able to change value! 
    if searchType == "1" or searchType == "2" or searchType == "3":
        #when search_type == "3" the user has chosen to exit, and if they did not provide a 1, 2, or 3 to search_type then they will automatically be brought back through the loop to see the menu again
        answer = input("Would you like to search again? [y/n]: ").lower()


print("\nThanks for using the search program. Goodbye!\n")