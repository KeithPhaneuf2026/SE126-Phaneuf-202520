#w4D1 - Sequential Search

#Program Prompt: We will continue to work with the class_grades.csv file, as used in the W3D2 demo. We will practice connecting to a file, storing the file data into parallel lists, and creating new data for each student record based on these lists. We will then build a sequential search program which will allow us to find students in the file, and write data regarding them to a newly created file in our repository.

#Imports
import csv
#Functions
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "ERROR"

    return let #the 'let' value will literally replace the letter() call in the main code
#Main Code

#Create some empty lists - one list for every potential field in the file
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

#connecting to file
with open("Week 3/W3D2 class lab/class_grades.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:        
        #store data from current record to corresponding lists (each field on its own)
        #.append --> data dispersed across lists, connected by the same index
        
        #parallel lists --> data dispersed across lists, connected by the same index
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#Disconnected from file

#Process the list to create and store each student's numeric average as well as letter grade average, the display all data back to the user

num_avg = []        #holds student's numeric avg: (test1 + test2 + test3) / 3
let_avg = []        #holds student's letter avg: letter(num_avg) return

for i in range(0, len(firstName)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)
    let_avg.append(letter(a))

print(f"{'FIRST':10}  {'LAST':10}   {'T1':3}  {'T2':3}  {'T3':3}   {'# AVG':6}  {'L AVG'}")
print("------------------------------------------------------")

for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}  {lastName[i]:10}  {test1[i]:3}  {test2[i]:3}  {test3[i]:3}  {num_avg[i]:6.1f}    {let_avg[i]}")
print("------------------------------------------------------")
print(f"TOTAL STUDENTS IN FILE: {len(firstName)}")

#sequential search - search for a student by their last name

#step 1: set-up and gain search query
found = -1  #flag var, will be replaced with index position if name is found
search_last = input("Enter the last name you wish to find: ")

#step 2: perform search algo (seq. search -> for loop w/ if statement)
for i in range(0, len(lastName)):
    #for loop performs sequence - from start through end of list

    if search_last.lower() == lastName[i].lower():
        #if performs the search - is what we're looking for here in he list?
        found = i #stores found item's INDEX LOCATION

#step 3: display results o user; make sure you give info: both for found or NOT found
if found != -1:
    #last name FOUND!
    print(f"Your search for {search_last} was FOUND! Here is their data: ")
    print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}    {let_avg[found]}")
else:
    #NOT FOUND
    print(f"Your search for {search_last} was NOT FOUND!")
    print("Check your cAsInG and sPeLlInG and try again!")