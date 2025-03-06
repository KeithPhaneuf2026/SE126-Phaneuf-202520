#Keith Phaneuf
#SE126.04
#Final Lab
#3-5-2025 [W9D1]

#PROGRAM PROMPT:
'''
Make a program that will sort through a populated csv file of almost all cars sold in the US in 2025 that are sold starting under $70,000.

Goals of this project:
    -Display list of make, model, class, price, horsepower, torque, engine, efficiency, and aspiration. 
    -use sequential and binary search to search for vehicles by make, make and model, class, price range, horsepower range, engine size, cylinder count, fuel economy or range, and aspiration type. 
'''

#variable dictionary
#totalRecords    counts total number of books

#imports
import csv

#lists
make = []
model = []
vehicleClass = []
price = []
horsepower = []
torque = []
engine = []
efficiency = []
aspiration = []

#connected
totalRecords = 0

with open("Week 8/Final Lab/2025CarList.csv") as csvfile: #opens csv file
    file = csv.reader(csvfile)

    for rec in file:
        totalRecords += 1
        make.append(rec[0])
        model.append(rec[1])
        vehicleClass.append(rec[2])
        price.append(rec[3])
        horsepower.append(rec[4])
        torque.append(rec[5])
        engine.append(rec[6])
        efficiency.append(rec[7])
        aspiration.append(rec[8])

#disconnected
#prints header
print(f"{'MAKE':12} {'MODEL':20} {'CLASS':25} {'PRICE':10}  {'HORSEPOWER':12} {'TORQUE':7} {'ENGINE':15} {'EFFICIENCY':20} {'ASPIRATION'}")
print("-" * 150)
for index in range(0,len(make)):
    print(f"{make[index]:12} {model[index]:20} {vehicleClass[index]:25} ${price[index]:10} {horsepower[index]:12} {torque[index]:7} {engine[index]:15} {efficiency[index]:20} {aspiration[index]}")
print("-" * 150)

#searching
ans = input("Would you like to enter the Personal Library Menu? [y/n]").lower()

#validity and user error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the Personal Library Menu? [y/n]").lower()

#main searching loop
while ans == "y":
    found = [] #reset found list so each new menu/search it is empty

    print("\n\tSEARCHING MENU")
    print("1: Show All Titles: ")
    print("2: Search by Title: ")
    print("3: Search by Author: ")
    print("4: Search by Genre: ")
    print("5: Search by Library Number: ")
    print("6: Show All Available: ")
    print("7: Show All On Loan: ")
    print("8: Exit")

    search = input("\nHow would you like to search today? [1-8]: ")

    #using 'not in' for user validity checks
    if search not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
         print("***INVALID ENTRY!***\nPlease try again")

    elif search == "1":#displays all books on file
        print("Squak")