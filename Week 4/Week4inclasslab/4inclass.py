#Keith Phaneuf
#SE126.04
#Lab 2
#1-27-2025 [W4D1]

#PROGRAM PROMPT:
'''Part 1

Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.

Original File Headers

FIELD0             FIELD1            FIELD2       FIELD3        FIELD4     

Firstname          Lastname        Test1         Test2             Test3

 

Part 2

Next, reprocess the lists to find each student's current average score, letter grade equivalent, and the class average.  While processing in the for loop, store each student's average into a new list called 'num_avg' and their letter grade into a list called 'let_avg'. Then, print each student's full information, record by record including average score and average letter equivalent.  After this print of the original file data from the lists, print to the console the total number of student's in the class along with the class numeric average.  

 

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

print(f"\nTOTAL RECORDS: {total_records}\nCURRENT CLASS AVERAGE: {class_avg:.2f}\n\nGoodbye!")