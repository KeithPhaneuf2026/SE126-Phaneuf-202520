#Keith Phaneuf
#SE126.04
#Lab 7
#2-27-2025 [W8D2]

#PROGRAM PROMPT:
'''
Build a mini programming dictionary a user can search through and ad to using the words.csv file:
words.csv fields
Field #	File Data
0	Word (unique)
1	Definition

Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a user to interact with the dictionary based on the following menu: 
My Programming Dictionary Menu
1.	Show all words – Show all words and their definitions stored to the dictionary
2.	Search for a word – Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if the word is not in the dictionary)
3.	Add a word – Allow a user to add a word and its definition to the dictionary if it does not already exist
4.	EXIT
The program should not be case sensitive for user input, and the user should only be able to quit when they have selected menu option number 4.

Bonus #1 [+5]: When the user is finished using the program, create a new file called updated_words.csv which contains the entire dictionary (including any new words added during the session) and follows the original words.csv field structure (first field is the word, second field is the definition).

Bonus #2 [+10]: Add a menu option “3.5” which will show all of the words in the dictionary, ordered alphabetically in ascending order (A -> Z) 
'''
#Variable Dictionary
#dictionary             dictionary of csv
#newDictionary          2d list, used for bubble sort including added words
#word                   first list, used for utilizing length of list
#ans                    a y or n response for using the searching program
#found                  holds search results or used to change if value is found to end if statements
#searchType             method of search input by user
#searchWord             used to search by word
#appendWord             collects new word to be added to dictionary and 2d list
#appendDef              collects new definition for word from appendWord to be added to dictionary and 2d list
#temp                   used for bubble sort

#imports
import csv
#lists
dictionary = {}
newDictionary = []

#connected
with open("Week 8/Lab 7/words.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        dictionary.update({rec[0] : rec[1]})
        newDictionary.append(rec)#adds same data to 2d list


#disconnected
#prints header
print(f"{'Word':14} : {'Definition'}")
print("-" * 150)
for word in dictionary:
    #for every key found in library dictionary
    print(f"{word.upper():14} : {dictionary[word]}")
print("-" * 150)

#Dictionary Searching Program
ans = input("Would you like to enter the Dictionary Searching Program? [y/n]").lower()

#validity and user error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the Dictionary Searching Program? [y/n]").lower()

#main searching loop
while ans == "y":
    found = [] #reset found list so each new menu/search it is empty

    #searching menu
    print("\n\tSEARCHING MENU")
    print("1: Show All Words: ")
    print("2: Search for a word: ")
    print("3: Add a word: ")
    print("3.5: Show All words organized alphabetically in ascending order (A-Z): ")
    print("4: EXIT ")

    searchType = input("\nHow would you like to search today? [1-4]: ")

    #using 'not in' for user validity checks
    if searchType not in ["1", "2", "3", "3.5", "4"]:
         print("***INVALID ENTRY!***\nPlease try again")

    elif searchType == "1":#displays all words on file
        print("Displaying All Words: ")
        print(f"{'Word':14} : {'Definition'}")
        print("-" * 150)
        for word in dictionary:
            #for every key found in library dictionary
            print(f"{word.upper():14} : {dictionary[word]}")
        print("-" * 150)

    elif searchType == "2":#searches for a specific word
        print("Searching for a word: ")
        found = 0
        searchWord = input("\nEnter the WORD you are looking for: ")
        for word in dictionary:
            if searchWord.lower() == word.lower():
                found = word

        if found != 0:
            print(f"We found your search for {searchWord}, here is the info: ")
            print("-" * 150)
            print(f"{found.upper():14} : {dictionary[found]}")
            print("-" * 150)
        else:
            print(f"We could not find your search for {searchWord}. Please check spelling:  ")
    
    elif searchType == "3":#adds a word to the list
        print("Adding a word to the list: ")

        appendWord = input("Please input the word you are going to add to the dictionary: ")
        appendDef = input("Please enter the definition of the word you have just entered: ")
        dictionary.update({appendWord : appendDef})#updates dictionary
        newDictionary.append([appendWord, appendDef])#updates 2d list
        print(f"{'Word':14} : {'Definition'}")
        print("-" * 150)
        for word in dictionary:
            #for every key found in library dictionary
            print(f"{word.upper():14} : {dictionary[word]}")
        print("-" * 150)

    elif searchType == "3.5":#presents ordered lists of words by alphabetical order (A-Z)
        print("Show All words organized alphabetically in ascending order (A-Z): ")
        #bubble sort
        for i in range(len(newDictionary) - 1):
            for j in range(len(newDictionary) - 1):
                if newDictionary[j][0] > newDictionary[j + 1][0]:
                    temp = newDictionary[j][0]
                    newDictionary[j][0] = newDictionary[j+1][0]
                    newDictionary[j+1][0] = temp
                    temp = newDictionary[j][1]
                    newDictionary[j][1] = newDictionary[j+1][1]
                    newDictionary[j+1][1] = temp
        
        #prints header
        print(f"{'Word':14} : {'Definition'}")
        print("-" * 150)
        for i in range(0, len(newDictionary)):
            print(f"{newDictionary[i][0]:14} : {newDictionary[i][1]}")
        print("-" * 150)

    elif searchType == "4":#exit
        ans = "n"

    else:
        print("\nINVALID ENTRY!!!") #if searchType input isnt 1-4

print("Thank you for using the Personal Library Menu. Have a great day!")#end statement

#opens midterm_choice2.csv
file = open("Week 8/Lab 7/updated_words.csv", "w")
for word in dictionary:
    file.write(f"{word}, {dictionary[word]} \n")
file.close()