#Keith Phaneuf
#SE126.04
#Lab 5
#2-13-2025 [W6D2]

#PROGRAM PROMPT:
'''
Build a personal library search system using the file book_list.csv. It is set up as follows:
book_list.csv fields
Field #	File Data
0	Library Number (unique)
1	Title
2	Author
3	Genre
4	Page Count
5	Status: Available/On Loan

Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options.  Your program should give your user the following menu:
Personal Library Menu
1.	Show All Titles – list all book data to the user alphabetically by title
2.	Search by Title – allow for an entire title or a title key word
3.	Search by Author – show all titles of the searched-for author
4.	Search by Genre - show all titles of the searched-for genre
5.	Search by Library Number – only allow for one specific library number item
6.	Show All Available – show all titles with status “available”
7.	Show All On Loan - show all titles with status “on loan”
8.	EXIT
When your user runs any of the options 1 - 7, show all data associated with the search [Library Number, Title, Author, Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches should not be case sensitive.
'''

#variable dictionary
'''
libraryNumber   stores library number of each book
title           stores book titles
author          stores author names
genre           stores genres of books
pageCount       stores number of pages
status          stores status of books if they are on loan or available
ans             if "y", user can use book search program
searchType      determines method of search, either title or author; can also be used to quit program
searchTitle     collects user input for search of book title
searchAuthor    collects user input for search of author
searchGenre     collects user input for search of genre
searchLibrary   collects user input for search of library number
searchStatus    is made either 'on loan' or 'available' for search selection
totalRecords    counts total number of books
found           holds search results of title, author, genre, library, on loan, or available
min             minimum index in bubble sort
max             maximum index in bubble sort
mid             middle index of bubble sort
'''

#imports
import csv

#functions
def swap(index, listName): #bubble sort
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp



#lists
libraryNumber = []
title = []
author = []
genre = []
pageCount = []
status = []

#connected
totalRecords = 0

with open ("Week 6/Lab #5/book_list.csv") as csvfile: #opens csv file
    file = csv.reader(csvfile)

    for rec in file:
        totalRecords += 1
        libraryNumber.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        pageCount.append(rec[4])
        status.append(rec[5])

#Personal Library Menu
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

    searchType = input("\nHow would you like to search today? [1-8]: ")

    #using 'not in' for user validity checks
    if searchType not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
         print("***INVALID ENTRY!***\nPlease try again")

    elif searchType == "1":#displays all books on file
        print("Displaying All Titles: ")

        #prints header
        print(f"{'Library Number':16}  {'Title':35}  {'Author':15}  {'Genre':15}  {'Pages':5}  {'Status'}")
        print("---------------------------------------------------------------------------------------------------------")

        for index in range(0, len(libraryNumber)):#displays all books on file
            print(f"{libraryNumber[index]:16}  {title[index]:35}  {author[index]:15}  {genre[index]:15}  {pageCount[index]:5}  {status[index]}")
        print(f"Total number of books on file: {totalRecords}")

    elif searchType == "2":
        print("Searching by Title: ")
        #bubble sort
        for i in range(len(title) - 1):
            for j in range(len(title) - 1):
                if title[j] > title[j + 1]:
                    #swap
                    swap(j, libraryNumber)
                    swap(j, title)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, pageCount)
                    swap(j, status)

        #binary search
        searchTitle = input("Enter the TITLE of the book you wish to search: ")
        min = 0                     #first index
        max = len(title) - 1         #last index
        mid = int((min + max) / 2)    #middle index

        while min < max and searchTitle.lower() != title[mid].lower():
            if searchTitle.lower() < title[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1

            mid = int((min+max) / 2)
            
        if searchTitle.lower() == title[mid].lower():
            print(f"Your search for {searchTitle} was found. See details below: \n")
            #prints header
            print(f"{'Library Number':16}  {'Title':35}  {'Author':15}  {'Genre':15}  {'Pages':5}  {'Status'}")
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{libraryNumber[mid]:16}  {title[mid]:35}  {author[mid]:15}  {genre[mid]:15}  {pageCount[mid]:5}  {status[mid]}")#for one book
        else:
            print(f"Your search for {searchTitle} was NOT FOUND! Please check spelling and try again!")

    elif searchType == "3":
        print("Searching by Author: ")

        searchAuthor = input("Enter the AUTHOR NAME you wish to search: ")
        
        for i in range(0, len(author)):  #searches through authors
            if searchAuthor.lower() == author[i].lower():
                found.append(i)
        if not found:
            print(f"\nYour search for {searchAuthor} was NOT FOUND! Please check spelling and try again!\n")     
        else:
            print(f"Your search for {searchAuthor} was found. See details below: \n")
            #prints header
            print(f"{'Library Number':16}  {'Title':35}  {'Author':15}  {'Genre':15}  {'Pages':5}  {'Status'}")
            print("---------------------------------------------------------------------------------------------------------")
            for i in range (0, len(found)):#for multiple items
                print(f"{libraryNumber[found[i]]:16}  {title[found[i]]:35}  {author[found[i]]:15}  {genre[found[i]]:15}  {pageCount[found[i]]:5}  {status[found[i]]}")

    elif searchType == "4":
        print("Searching by Genre")

        searchGenre = input("Enter the GENRE you wish to search: ")

        for i in range(0, len(genre)):  #searches through authors
            if searchGenre.lower() == genre[i].lower():
                found.append(i)
        if not found:
            print(f"\nYour search for {searchGenre} was NOT FOUND! Please check spelling and try again!\n")     
        else:
            print(f"Your search for {searchGenre} was found. See details below: \n")
            #prints header
            print(f"{'Library Number':16}  {'Title':35}  {'Author':15}  {'Genre':15}  {'Pages':5}  {'Status'}")
            print("---------------------------------------------------------------------------------------------------------")
            for i in range (0, len(found)):#for multiple items
                print(f"{libraryNumber[found[i]]:16}  {title[found[i]]:35}  {author[found[i]]:15}  {genre[found[i]]:15}  {pageCount[found[i]]:5}  {status[found[i]]}")

    elif searchType == "5":
        print("Searching by Library Number: ")

        #bubble sort
        for i in range(len(libraryNumber) - 1):
            for j in range(len(libraryNumber) - 1):
                if libraryNumber[j] > libraryNumber[j + 1]:
                    #swap
                    swap(j, libraryNumber)
                    swap(j, title)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, pageCount)
                    swap(j, status)

        #binary search
        searchLibrary = input("Enter the Library Number of the book you wish to search: ")
        min = 0                         #first index
        max = len(libraryNumber) - 1    #last index
        mid = int((min + max) / 2)      #middle index

        while min < max and searchLibrary.lower() != libraryNumber[mid].lower():
            if searchLibrary.lower() < libraryNumber[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1

            mid = int((min+max) / 2)
            
        if searchLibrary.lower() == libraryNumber[mid].lower():
            print(f"Your search for {searchLibrary} was found. See details below: \n")
            #prints header
            print(f"{'Library Number':16}  {'Title':35}  {'Author':15}  {'Genre':15}  {'Pages':5}  {'Status'}")
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{libraryNumber[mid]:16}  {title[mid]:35}  {author[mid]:15}  {genre[mid]:15}  {pageCount[mid]:5}  {status[mid]}")#prints book
        else:
            print(f"Your search for {searchLibrary} was NOT FOUND! Please check spelling and try again!")

    elif searchType == "6":
        print("Showing All Available: ")

        searchStatus = "available"

        for i in range(0, len(status)):  #searches through authors
            if searchStatus.lower() == status[i].lower():
                found.append(i)
        if not found:
            print(f"\nYour search for {searchStatus} was NOT FOUND! Please check spelling and try again!\n")     
        else:
            print(f"Showing all books Available: \n")
            #prints header
            print(f"{'Library Number':16}  {'Title':35}  {'Author':15}  {'Genre':15}  {'Pages':5}  {'Status'}")
            print("---------------------------------------------------------------------------------------------------------")
            for i in range (0, len(found)):#for multiple items
                print(f"{libraryNumber[found[i]]:16}  {title[found[i]]:35}  {author[found[i]]:15}  {genre[found[i]]:15}  {pageCount[found[i]]:5}  {status[found[i]]}")

    elif searchType == "7": #displays books on loan
        print("Showing All On Loan: ")

        searchStatus = "on loan"

        for i in range(0, len(status)):  #searches through authors
            if searchStatus.lower() == status[i].lower():
                found.append(i)
        if not found: #if none on loan
            print(f"\nYour search for {searchStatus} was NOT FOUND! Please check spelling and try again!\n")     
        else:
            print(f"Showing all books On Loan \n")
            #prints header
            print(f"{'Library Number':16}  {'Title':35}  {'Author':15}  {'Genre':15}  {'Pages':5}  {'Status'}")
            print("---------------------------------------------------------------------------------------------------------")
            for i in range (0, len(found)):#for multiple items
                print(f"{libraryNumber[found[i]]:16}  {title[found[i]]:35}  {author[found[i]]:15}  {genre[found[i]]:15}  {pageCount[found[i]]:5}  {status[found[i]]}")

    elif searchType == "8":
        ans = "n"

    else:
        print("\nINVALID ENTRY!!!") #if searchType input isnt 1-8
    if searchType == "1" or searchType == "2" or searchType == "3" or searchType == "4" or searchType == "5" or searchType == "6" or searchType == "7":  #allows user to keep using program and/or exit
        ans = input("Would you like to search again? [Y/N]: ").lower()

print("Thank you for using the Personal Library Menu. Have a great day!")#end statement