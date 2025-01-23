#W3D2 - List Review - 1Dimensional Lists and Parallel Lists

#Prompt: Our W3D2 demo will focus on reviewing accessing text file data and storing the data into 1d lists. We will store the file data into respective lists, then process the data to print the information for each student as well as calculate and store a new peice of data for each student: their current average test score.

#this file uses: class_grades.csv

#--imports------------------------
import csv
#--Functions----------------------

#--Main Code----------------------

#initialize a record counting variable
total_records = 0

#create an empty list for every potential field
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []


#connecting to file
with open("Week 3/W3D2 class lab/class_grades.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        
        total_records += 1

        #fname = rec[]

        #print(fname)
        
        #store data from current record to corresponding lists (each field on its own)
        #.append --> data dispersed across lists, connected by the same index
        
        #parallel lists --> data dispersed across lists, connected by the same index
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#disconnected from file

#processing lists -- Use a for loop
#for index in range(0, len(firstName)):
    #for every item, index will start at 0 and run up to (not including) the length (# of items)
    #print(f"INDEX {index:3}: Student {index+1:3}: {firstName[index]:10}  {lastName[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3}")

#create a list to hold each student's avg test score
avg = []

for i in range(0, len(test1)):

    a= (test1[i] + test2[i] + test3[i]) / 3
    avg.append(a)

print(f"INDEX #:                {'FIRST':10}  {'LAST':10}   {'T1':3}  {'T2':3}  {'T3':3} {'AVG'}")
print("-----------------------------------------------------------------------------")
for index in range(0, len(firstName)):
    #for every item, index will start at 0 and run up to (not including) the length (# of items)
    print(f"INDEX {index:3}: Student {index+1:3}: {firstName[index]:10}  {lastName[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3}  {avg[index]:.2f}")
print("-----------------------------------------------------------------------------")

#calc the entire class average using a for loop to add each student's avg to the class total
total_avg = 0
for i in range(0, len(avg)):
    total_avg += avg[i]

class_avg = total_avg / len(avg)

print(f"\nTOTAL RECORDS: {total_records}\nCURRENT CLASS AVERAGE: {class_avg:.2f}\n\nGoodbye!")