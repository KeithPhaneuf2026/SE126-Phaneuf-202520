#Keith Phaneuf
#SE126.04
#Lab 2
#1-27-2025 [W4D1]

#PROGRAM PROMPT:
'''(Source: QBasic Fundamentals and Style, Quasney, Maniotes, Foremant; P. 190 #3)

Construct a program that will analyze potential voters. The program should generate the following totals:

Number of individuals not eligible to register.
Number of individuals who are old enough to vote but have not registered.
Number of individuals who are eligible to vote but did not vote.
Number of individuals who did vote.
Number of records processed'''

#Variable Dictionary
#total_rec          total number of computers
#idNumbers          holds id numbers
#age                holds ages of people in file
#registered         holds registration status
#voted              holds vote status
#tooYoung           counts how many people are too young to register
#oldNoRegi          counts how many people are old enough but not registered voters
#totalRegistered    counts how many people are registered voters but didn't vote
#voted              counts how many people voted

#Imports
import csv

#Connected to file
total_rec = 0 #used to count computers

#Lists
idNumbers = []
age = []
registered = []
voted = []

#variables
tooYoung = 0
oldNoRegi = 0
totalRegistered = 0
totalVoted = 0

#connected to file
with open("Week 3/Lab #3/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        total_rec += 1
        idNumbers.append(int(rec[0]))
        age.append(int(rec[1]))
        registered.append(rec[2])
        voted.append(rec[3])
        #counts all voter stats to determine how many people can't register to vote, can register but haven't, and vote but didn't, and voted
        if int(rec[1]) >= 18 and rec[3] == "Y":
            totalVoted += 1
        elif int(rec[1]) >= 18 and rec[2] == "Y" and rec[3] == "N":
            totalRegistered += 1
        elif int(rec[1]) >= 18 and rec[2] == "N":
            oldNoRegi += 1
        elif int(rec[1]) < 18 :
            tooYoung += 1
print("ID Numbers:        Age:     Registered:    Voted:      ") #displays data
for index in range(0, len(idNumbers)):
    #for every item, index will start at 0 and run up to (not including) the length (# of items)
 
    print(f"{idNumbers[index]:14}     {age[index]:6}              {registered[index]:6}    {voted[index]:5}      ") #displays data

#displays final numbers
print(f"\nNumber of people who are not old enough to vote:                                 {tooYoung}")
print(f"\nNumber of people who are old enough to vote but are not registered:              {oldNoRegi}")
print(f"\nNumber of people who are old enough to vote and are registered, but didn't vote: {totalRegistered}")
print(f"\nNumber of people who are old enough to vote and voted:                           {totalVoted}")
print(f"\nTotal number of records:                                                         {total_rec}")