#Keith Phaneuf
#SE126.04
#Final Lab
#3-5-2025 [W9D1]

#PROGRAM PROMPT:
'''
Make a program that will sort through a populated csv file of almost all cars sold in the US in 2025 that are sold starting under $70,000.

Goals of this project:
    -Display list of make, model, class, price, horsepower, torque, engine, efficiency, and aspiration. 
    -use sequential and binary search to search for vehicles by make, make and model, class, price range, horsepower range, cylinder count, fuel economy or range, and aspiration type. 
'''

#variable dictionary
#totalRecords    counts total number of books

#imports
import csv

#functions
def swap(index, listName): #bubble sort
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

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
    print("1: Display All Vehicles: ")
    print("2: Search by Make: ")
    print("3: Search by Model: ")
    print("4: Search by Vehicle Class: ")
    print("5: Search by Price Range: ")
    print("6: Search by Engine: ")
    print("7: Search by Cylinder Count: ")
    print("8: Search by Fuel Economy or Range: ")
    print("9: Search by Aspiration: ")
    print("10: Exit")

    search = input("\nHow would you like to search today? [1-10]: ")

    #using 'not in' for user validity checks
    if search not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
         print("***INVALID ENTRY!***\nPlease try again")

    elif search == "1":#displays all vehicles on file
        print("Displaying all vehicles")

        #prints header
        print(f"{'MAKE':12} {'MODEL':20} {'CLASS':25} {'PRICE':10}  {'HORSEPOWER':12} {'TORQUE':7} {'ENGINE':15} {'EFFICIENCY':20} {'ASPIRATION'}")
        print("-" * 150)
        for index in range(0,len(make)):
            print(f"{make[index]:12} {model[index]:20} {vehicleClass[index]:25} ${price[index]:10} {horsepower[index]:12} {torque[index]:7} {engine[index]:15} {efficiency[index]:20} {aspiration[index]}")
        print("-" * 150)

    elif search == "2":#Sequential
        print("Searching by Make: ")
        searchMake = input("Enter the MAKE you wish to search: ")
        
        for i in range(0, len(make)):  #searches through authors
            if searchMake.lower() == make[i].lower():
                found.append(i)
        if not found:
            print(f"\nYour search for {searchMake} was NOT FOUND! Please check spelling and try again!\n")     
        else:
            print(f"Your search for {searchMake} was found. See details below: \n")
            #prints header
            print(f"{'MAKE':12} {'MODEL':20} {'CLASS':25} {'PRICE':10}  {'HORSEPOWER':12} {'TORQUE':7} {'ENGINE':15} {'EFFICIENCY':20} {'ASPIRATION'}")
            print("-" * 150)
            for i in range(0,len(found)):
                print(f"{make[found[i]]:12} {model[found[i]]:20} {vehicleClass[found[i]]:25} ${price[found[i]]:10} {horsepower[found[i]]:12} {torque[found[i]]:7} {engine[found[i]]:15} {efficiency[found[i]]:20} {aspiration[found[i]]}")
            print("-" * 150)
            
    elif search == "3":#binary
        print("Searching by Model: ")
        
        #bubble sort
        for i in range(len(model) - 1):
            for j in range(len(model) - 1):
                if model[j] > model[j + 1]:
                    #swap
                    swap(j, make)
                    swap(j, model)
                    swap(j, vehicleClass)
                    swap(j, price)
                    swap(j, horsepower)
                    swap(j, torque)
                    swap(j, engine)
                    swap(j, efficiency)
                    swap(j, aspiration)
        
        searchModel = input("Enter the Model you wish to search: ")
        min = 0                     #first index
        max = len(model) - 1         #last index
        mid = int((min + max) / 2)    #middle index

        while min < max and searchModel.lower() != model[mid].lower():
            if searchModel.lower() < model[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1

            mid = int((min+max) / 2)
            
        if searchModel.lower() == model[mid].lower():
            print(f"Your search for {searchModel} was found. See details below: \n")
            #prints header
            print(f"{'MAKE':12} {'MODEL':20} {'CLASS':25} {'PRICE':10}  {'HORSEPOWER':12} {'TORQUE':7} {'ENGINE':15} {'EFFICIENCY':20} {'ASPIRATION'}")
            print("-" * 150)
            print(f"{make[mid]:12} {model[mid]:20} {vehicleClass[mid]:25} ${price[mid]:10} {horsepower[mid]:12} {torque[mid]:7} {engine[mid]:15} {efficiency[mid]:20} {aspiration[mid]}")
            print("-" * 150)
        else:
            print(f"\nYour search for {searchModel} was NOT FOUND! Please check spelling and try again!\n")     
    
    elif search == "4":#sequential
        print("Searching by Vehicle Class: \n")
        print("Vehicle Classes: \n\nSubcompact Crossover SUV\nCompact Crossover SUV\nCompact SUV\nMidsize Crossover SUV\nMidsize SUV\nFullsize SUV\nSubcompact Sedan\nCompact Sedan\nMidsize Sedan\nFullsize Sedan\nMidsize Wagon\nHatchback\nMinivan\nCompact Pickup\nMidsize Pickup\nFullsize Pickup\n3/4 Ton Pickup\nCoupe\nVan")
        searchClass = input("Enter the VEHICLE CLASS you wish to search: ")
        
        for i in range(0, len(vehicleClass)):  #searches through authors
            if searchClass.lower() == vehicleClass[i].lower():
                found.append(i)
        if not found:
            print(f"\nYour search for {searchClass} was NOT FOUND! Please check spelling and try again!\n")     
        else:
            print(f"Your search for {searchClass} was found. See details below: \n")
            #prints header
            print(f"{'MAKE':12} {'MODEL':20} {'CLASS':25} {'PRICE':10}  {'HORSEPOWER':12} {'TORQUE':7} {'ENGINE':15} {'EFFICIENCY':20} {'ASPIRATION'}")
            print("-" * 150)
            for i in range(0,len(found)):
                print(f"{make[found[i]]:12} {model[found[i]]:20} {vehicleClass[found[i]]:25} ${price[found[i]]:10} {horsepower[found[i]]:12} {torque[found[i]]:7} {engine[found[i]]:15} {efficiency[found[i]]:20} {aspiration[found[i]]}")
            print("-" * 150)

    elif search == "5":#sequential
        print("Searching by Price Range: ")
        
        #bubble sort
        for i in range(len(price) - 1):
            for j in range(len(price) - 1):
                if price[j] > price[j + 1]:
                    #swap
                    swap(j, make)
                    swap(j, model)
                    swap(j, vehicleClass)
                    swap(j, price)
                    swap(j, horsepower)
                    swap(j, torque)
                    swap(j, engine)
                    swap(j, efficiency)
                    swap(j, aspiration)
        
        searchPrice = input("Enter the MAX PRICE for a vehicle you wish to purchase: $")
        
        for i in range(0, len(price)):  #searches through authors
            if searchPrice >= price[i]:
                found.append(i)
        if not found:
            print(f"\nYour search for {searchPrice} was NOT FOUND! Please check spelling and try again!\n")     
        else:
            print(f"Your search for {searchPrice} was found. See details below: \n")
            #prints header
            print(f"{'MAKE':12} {'MODEL':20} {'CLASS':25} {'PRICE':10}  {'HORSEPOWER':12} {'TORQUE':7} {'ENGINE':15} {'EFFICIENCY':20} {'ASPIRATION'}")
            print("-" * 150)
            for i in range(0,len(found)):
                print(f"{make[found[i]]:12} {model[found[i]]:20} {vehicleClass[found[i]]:25} ${price[found[i]]:10} {horsepower[found[i]]:12} {torque[found[i]]:7} {engine[found[i]]:15} {efficiency[found[i]]:20} {aspiration[found[i]]}")
            print("-" * 150)

    elif search == "6":#sequential
        print("Search by Engine: ")

        searchEngine = input("Enter the Engine you wish to search: ")
    elif search == "7":#sequential
        print("Searching by Cylinder Count: ")
    elif search == "8":#sequential
        print("Searching by Fuel Economy or Range")
    elif search == "9":#sequential
        print("Searching by Aspiration: ")
    elif search == "10":#exit
        ans = "n"

    else:
        print("\nINVALID ENTRY!!!") #if searchType input isnt 1-8
    if search == "1" or search == "2" or search == "3" or search == "4" or search == "5" or search == "6" or search == "7" or search == "8" or search == "9":  #allows user to keep using program and/or exit
        ans = input("Would you like to search again? [Y/N]: ").lower()

print("Thank you for using the Personal Library Menu. Have a great day!")#end statement