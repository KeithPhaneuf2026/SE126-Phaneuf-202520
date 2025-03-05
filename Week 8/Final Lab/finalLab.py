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
print(f"{'MAKE':15} {'MODEL':20} {'CLASS':15} {'STARTING PRICE':10} {'HORSEPOWER':5} {'TORQUE':5} {'ENGINE'} {'EFFICIENCY':15} {'ASPIRATION'}")