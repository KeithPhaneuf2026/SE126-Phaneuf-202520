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
#totalRecords       counts total number of books
#make               list of vehicle makes
#model              list of vehicle models
#vehicleClass       list of vehicle classes
#price              list of vehicle starting prices
#horsepower         list of vehicle horsepower outputs
#torque             list of vehicle torque outputs by lb-ft
#engine             list of vehicle engines
#efficiency         list of vehicle energy efficiency
#aspiration         list of vehicle aspirations / methods of air induction
#ans                a y or n answer for use of program
#search             1-9 answer for method of search
#found              holds found items from lists
#searchMake         used to collect make search
#searchModel        used to collect model search
#searchClass        used to collect vehicle class
#searchPrice        used to collect max purchase price
#searchEngine       used to search engine
#searchAir          used to search method of air injection
#min                min index value for binary search
#max                max index value for binary search
#mid                mid index value for binary search

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

    for rec in file:#puts data frm csv file to lists
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
ans = input("Would you like to enter the Car Search Program? [y/n]").lower()

#validity and user error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the Car Search Program? [y/n]").lower()

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
    print("7: Sort by Highest Fuel Economy or Range: ")
    print("8: Search by Aspiration: ")
    print("9: Exit")

    search = input("\nHow would you like to search today? [1-9]: ")

    #using 'not in' for user validity checks
    if search not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
         print("***INVALID ENTRY!***\nPlease try again")

    elif search == "1":#displays all vehicles on file
        print("Displaying all vehicles")

        #prints header
        print(f"{'MAKE':12} {'MODEL':20} {'CLASS':25} {'PRICE':10}  {'HORSEPOWER':12} {'TORQUE':7} {'ENGINE':15} {'EFFICIENCY':20} {'ASPIRATION'}")
        print("-" * 150)
        for index in range(0,len(make)):#prints full list of vehicles
            print(f"{make[index]:12} {model[index]:20} {vehicleClass[index]:25} ${price[index]:10} {horsepower[index]:12} {torque[index]:7} {engine[index]:15} {efficiency[index]:20} {aspiration[index]}")
        print("-" * 150)

    elif search == "2":#Sequential search of makes
        print("Searching by Make: ")
        searchMake = input("Enter the MAKE you wish to search: ")
        
        for i in range(0, len(make)): 
            if searchMake.lower() == make[i].lower():
                found.append(i)
        if not found:
            print(f"\nYour search for {searchMake} was NOT FOUND! Please check spelling and try again!\n")     
        else:
            print(f"Your search for {searchMake} was found. See details below: \n")
            #prints header
            print(f"{'MAKE':12} {'MODEL':20} {'CLASS':25} {'PRICE':10}  {'HORSEPOWER':12} {'TORQUE':7} {'ENGINE':15} {'EFFICIENCY':20} {'ASPIRATION'}")
            print("-" * 150)
            for i in range(0,len(found)):#prints cars of one make
                print(f"{make[found[i]]:12} {model[found[i]]:20} {vehicleClass[found[i]]:25} ${price[found[i]]:10} {horsepower[found[i]]:12} {torque[found[i]]:7} {engine[found[i]]:15} {efficiency[found[i]]:20} {aspiration[found[i]]}")
            print("-" * 150)
            
    elif search == "3":#binary search of models
        print("Searching by Model: ")
        
        #bubble sort
        for i in range(len(model) - 1):
            for j in range(len(model) - 1):
                if model[j].lower() > model[j + 1].lower():
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

        #binary search
        while min < max and searchModel.lower() != model[mid].lower():
            if searchModel.lower() < model[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1

            mid = int((min + max) / 2)

        #when value is found    
        if searchModel.lower() == model[mid].lower():
            print(f"Your search for {searchModel} was found. See details below: \n")
            #prints header
            print(f"{'MAKE':12} {'MODEL':20} {'CLASS':25} {'PRICE':10}  {'HORSEPOWER':12} {'TORQUE':7} {'ENGINE':15} {'EFFICIENCY':20} {'ASPIRATION'}")
            print("-" * 150)
            #prints one car
            print(f"{make[mid]:12} {model[mid]:20} {vehicleClass[mid]:25} ${price[mid]:10} {horsepower[mid]:12} {torque[mid]:7} {engine[mid]:15} {efficiency[mid]:20} {aspiration[mid]}")
            print("-" * 150)
        else:
            print(f"\nYour search for {searchModel} was NOT FOUND! Please check spelling and try again!\n")     
    
        #bubble sort to put lists back in original state
        for i in range(len(make) - 1):
            for j in range(len(make) - 1):
                if make[j] > make[j + 1]:
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

    elif search == "4":#sequential search of vehicle class
        print("Searching by Vehicle Class: \n")
        print("Vehicle Classes: \n\nSubcompact Crossover SUV\nCompact Crossover SUV\nCompact SUV\nMidsize Crossover SUV\nMidsize SUV\nFullsize SUV\nSubcompact Sedan\nCompact Sedan\nMidsize Sedan\nFullsize Sedan\nMidsize Wagon\nHatchback\nMinivan\nCompact Pickup\nMidsize Pickup\nFullsize Pickup\n3/4 Ton Pickup\nCoupe\nVan")#prints list of all car classes included in list
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
            for i in range(0,len(found)):#prints all cars of one class
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
            for i in range(0,len(found)):#prints list of cars under an input amount
                print(f"{make[found[i]]:12} {model[found[i]]:20} {vehicleClass[found[i]]:25} ${price[found[i]]:10} {horsepower[found[i]]:12} {torque[found[i]]:7} {engine[found[i]]:15} {efficiency[found[i]]:20} {aspiration[found[i]]}")
            print("-" * 150)

        #used to sort lists back to original state
        for i in range(len(model) - 1):
            for j in range(len(model) - 1):
                if model[j].lower() > model[j + 1].lower():
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

        for i in range(len(make) - 1):
            for j in range(len(make) - 1):
                if make[j] > make[j + 1]:
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

    elif search == "6":#sequential search of engine
        print("Search by Engine: ")

        searchEngine = input("Enter the Engine you wish to search [EX: 2.4 I4]: ")

        for i in range(0, len(price)):  #searches through authors
            if searchEngine.lower() == engine[i].lower():
                found.append(i)
        if not found:
            print(f"\nYour search for {searchEngine} was NOT FOUND! Please check spelling and try again!\n")     
        else:
            print(f"Your search for {searchEngine} was found. See details below: \n")
            #prints header
            print(f"{'MAKE':12} {'MODEL':20} {'CLASS':25} {'PRICE':10}  {'HORSEPOWER':12} {'TORQUE':7} {'ENGINE':15} {'EFFICIENCY':20} {'ASPIRATION'}")
            print("-" * 150)
            for i in range(0,len(found)):#prints cars with same engine or similar engines
                print(f"{make[found[i]]:12} {model[found[i]]:20} {vehicleClass[found[i]]:25} ${price[found[i]]:10} {horsepower[found[i]]:12} {torque[found[i]]:7} {engine[found[i]]:15} {efficiency[found[i]]:20} {aspiration[found[i]]}")
            print("-" * 150)

    elif search == "7":#sorts from worst to best fuel economy
        print("Sorting by Highest Fuel Economy or Range")

        for i in range(len(efficiency) - 1):
            for j in range(len(efficiency) - 1):
                if efficiency[j] < efficiency[j + 1]:
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

        #prints header
        print(f"{'MAKE':12} {'MODEL':20} {'CLASS':25} {'PRICE':10}  {'HORSEPOWER':12} {'TORQUE':7} {'ENGINE':15} {'EFFICIENCY':20} {'ASPIRATION'}")
        print("-" * 150)
        for index in range(0,len(make)):#prints cars sorted by fuel efficiency
            print(f"{make[index]:12} {model[index]:20} {vehicleClass[index]:25} ${price[index]:10} {horsepower[index]:12} {torque[index]:7} {engine[index]:15} {efficiency[index]:20} {aspiration[index]}")
        print("-" * 150)

        #used to sort lists back to original state
        for i in range(len(model) - 1):
            for j in range(len(model) - 1):
                if model[j].lower() > model[j + 1].lower():
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
                    
        for i in range(len(make) - 1):
            for j in range(len(make) - 1):
                if make[j] > make[j + 1]:
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
        
    elif search == "8":#sequential search for aspiration
        print("Searching by Aspiration: ")

        searchAir = input("Enter the Aspiration Method you wish to search: ")

        for i in range(0, len(price)):  #searches through authors
            if searchAir.lower() == aspiration[i].lower():
                found.append(i)
        if not found:
            print(f"\nYour search for {searchAir} was NOT FOUND! Please check spelling and try again!\n")     
        else:
            print(f"Your search for {searchAir} was found. See details below: \n")
            #prints header
            print(f"{'MAKE':12} {'MODEL':20} {'CLASS':25} {'PRICE':10}  {'HORSEPOWER':12} {'TORQUE':7} {'ENGINE':15} {'EFFICIENCY':20} {'ASPIRATION'}")
            print("-" * 150)
            for i in range(0,len(found)):#displays list of cars with searched method of air induction
                print(f"{make[found[i]]:12} {model[found[i]]:20} {vehicleClass[found[i]]:25} ${price[found[i]]:10} {horsepower[found[i]]:12} {torque[found[i]]:7} {engine[found[i]]:15} {efficiency[found[i]]:20} {aspiration[found[i]]}")
            print("-" * 150)

    elif search == "9":#exit
        ans = "n"

    else:
        print("\nINVALID ENTRY!!!") #if searchType input isnt 1-8
    if search == "1" or search == "2" or search == "3" or search == "4" or search == "5" or search == "6" or search == "7" or search == "8":  #allows user to keep using program and/or exit
        ans = input("Would you like to search again? [Y/N]: ").lower()
        while ans != "y" and ans != "n":
            print("***INVALID ENTRY!***")
            ans = input("Would you like to search again? [y/n]").lower()
print("Thank you for using the Car Search Program. Have a great day!")#end statement