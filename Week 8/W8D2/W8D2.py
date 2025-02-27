#W8D2 - Dictionary Review + Gaining data from text files
#this demo utilizes: dictionary_file.csv

#Imports
import csv
#Main code
library = {
    #'key : value
    "1230" : "Red Rising",
    "1231" : "The Little Prince"
}

with open("Week 8/W8D2/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        #for every record in file, do following
        #file --> 2d list, rec --> 1 record's data, also a list
        library.update({rec[0] : rec[1]})
        #library_num --> rec[0], a string
        #title --> rec[1], also a string

#disconnected from file

print(f"{'KEY':4} : {'TITLE'}")
print("-" * 50)
for key in library:
    #for every key found in library dictionary
    print(f"{key.upper():4} : {library[key]}")
print("-" * 50)

#sequential search with dictionaries
search = input("\nEnter the Library Number you are looking for: ")

found = 0

for key in library:
    if search.lower() == key.lower():
        found = key

if found != 0:
    print(f"We found your search for {search}, here is the info: ")
    print("-" * 50)
    print(f"{found.upper():4} : {library[found]}")
    print("-" * 50)
else:
    print(f"We could not find your search for {search} :[ ")

search = input("\nEnter the TITLE you are looking for: ")

found = []

for key in library:
    if search.lower() in library[key].lower():
        found.append(key)

if found != 0:
    print(f"We found your search for {search}, here is the info: ")
    print("-" * 50)
    for i in range(0, len(found)):
        print(f"{found[i].upper():4} : {library[found[i]]}")
    print("-" * 50)
else:
    print(f"We could not find your search for {search} :[ ")