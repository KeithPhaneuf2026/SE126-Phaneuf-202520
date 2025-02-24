#W8D1 - intro to dictionaries

#dictionaries in python arw a collection set similar to associative arrays in Javascript but also look similar to JS object builds

#imports

#main code

#dictionaries
myCar = {
    #key : value
    "make": "Ford",
    "model": "Focus SE Hatchback",
    "year": 2014,
    "name": "Gwendoline",
    "color": "black"
    #key names cannot be repeated / no duplicates of keys
}

print(myCar)

#view a specific value from the dictionary
print(f"My car is a {myCar["make"]} {myCar["model"]}. It is {myCar["color"]}.")

yourCar = {
    #key : value
    "make": "Buick",
    "model": "LaCrosse CX",
    "year": 2005,
    "name": "no",
    "color": "beige"
    #key names cannot be repeated / no duplicates of keys
}

print(yourCar)

#view a specific value from the dictionary
print(f"My car is a {yourCar["make"]} {yourCar["model"]}. It is {yourCar["color"]}.")

#add some data to a dictionary
yourCar["plate"] = "12345"

#or use the .update ({key:value}) method
yourCar.update({"wheels" : "4"})

for key in yourCar:
    #for every key stored to the yourCar dictionary
    print(f"{key.upper():10}\t{yourCar[key]}")