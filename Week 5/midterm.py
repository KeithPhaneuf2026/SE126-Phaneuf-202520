#Keith Phaneuf
#SE126.04 
#Midterm
#2/10/2025 

#Program Prompt: Choice 2: books
'''Utilizes the books.csv file.
Fields in File
Field 0 Field 1 Field 2 Field 3
Title Author Genre Pages
Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have
been fully populated with file data, create a new list to hold a “status” value for each book. Assign each
book a status value of “On Loan” or “Available” and store to the newly created list. Half of the books
should be “On Loan” and the other half should be “Available”  you can decide which books hold which
status as long as it is an even split between the two potential values. Once the new list is populated,
process through the five lists to display all of the data to the user as well as the total number of records
in the file.
Once all of the data has been displayed, write all of the list data to a new file called
midterm_choice2.csv, where each books information is found on one record in the file and their data
is separated by a comma (additional empty line in resulting file is okay).
Finally, create a sequential search program that allows a user to repeatedly search the book database
information stored in the lists based on the following menu:
Personal Library Search
1. Search by TITLE
2. Search by AUTHOR
3. EXIT
For option 1: When a searched-for item is found, print all data* in the program on the specific book
from the lists. If they are not found, alert the user.
For option 2: When a searched for item is found, print all data* in the program on all authors that match
the criteria. If no one matches the searched-for criteria, alert the user.
The user should not be able to quit the search program unless they choose option 3, to exit.
*All Data to print per employee if found:
title, author, genre, pages, status'''

#Variable dictionary
'''
title           stores book titles
author          stores author names
genre           stores genres of books
pages           stores number of pages
status          stores status of books if they are on loan or available
answer          if "y", user can use book search program
searchType      determines method of search, either title or author; can also be used to quit program
searchTitle     collects user input for search of book title
searchAuthor    collects user input for search of author
totalRecords    counts total number of books
'''

#imports
import csv

#lists
title = []
author = []
genre = []
pages = []
status = []

#connected
totalRecords = 0
#prints header
print(f"{'TITLE':25}  {'Author':15}  {'GENRE':15}  {'PAGES':10}  {'STATUS':25}")
print("----------------------------------------------------------------------------------")

with open ("Week 5/books.csv") as csvfile: 
    file = csv.reader(csvfile)
    
    for rec in file:
        totalRecords += 1
        title.append(rec[0])
        author.append(rec[1])
        genre.append(rec[2])
        pages.append(rec[3])
        if rec[2] == "fantasy":
            status.append("On Loan")
        elif rec[2] == "horror":
            status.append("On Loan")
        elif rec[2] == "thriller":
            status.append("On Loan")
        else:
            status.append("Available")

#prints all data stored in lists
for index in range(0, len(title)):
    print(f"{title[index]:25}  {author[index]:15}  {genre[index]:15}  {pages[index]:10}  {status[index]:25}")

#prints total number of books
print(f"Total Number of books: {totalRecords}")
#opens midterm_choice2.csv
file = open("Week 5/midterm_choice2.csv", "w")
for i in range(0, len(title)):
    file.write(f"{title[i]}, {author[i]}, {genre[i]}, {pages[i]}, {status[i]} \n")
file.close()

#sequential search
print("Welcome to the Book Search Program!\n")
answer = input("Would you like to search for a book? [Y/N]: ").lower()
while answer == "y":    #program runs while answer == "y"

    print("\nSEARCH MENU:\n")
    print("1: Search by TITLE: ")
    print("2: Search by AUTHOR: ")
    print("3: EXIT: \n")

    searchType = input("Enter your method of search: [1-3]: ") #collects method of search

    if searchType == "1":   #search by title
        print("Searching by TITLE\n")
        found = -1
        searchTitle = input("Enter the TITLE of the book you wish to search: ")
        for i in range(0, len(title)):  #searches through titles
            if searchTitle.lower() == title[i].lower():
                found = i
        if found != -1:
            print(f"\nYour search for {searchTitle} was FOUND! Here is its data: \n")
            print(f"{'TITLE':25}  {'Author':15}  {'GENRE':15}  {'PAGES':10}  {'STATUS':25}")
            print("----------------------------------------------------------------------------------")
            print(f"{title[found]:25}  {author[found]:15}  {genre[found]:15}  {pages[found]:10}  {status[found]:25}\n")
        else:
            print(f"Your search for {searchTitle} was NOT FOUND! Please check spelling and try again!")
    elif searchType == "2": #search by author
        print("Searching by AUTHOR\n")
        found = []  #can have multiple books from same author
        searchAuthor = input("Enter the AUTHOR NAME you wish to search: ")
        for i in range(0, len(title)):  #searches through authors
            if searchAuthor.lower() == author[i].lower():
                found.append(i)
        if not found:
            print(f"\nYour search for {searchAuthor} was NOT FOUND! Please check spelling and try again!\n")     
        else:
            print(f"Your search for {searchAuthor} was FOUND! Here is their data: \n")
            print(f"{'TITLE':25}  {'Author':15}  {'GENRE':15}  {'PAGES':10}  {'STATUS':25}")
            print("----------------------------------------------------------------------------------")
            for i in range (0, len(found)):
                print(f"{title[found[i]]:25}  {author[found[i]]:15}  {genre[found[i]]:15}  {pages[found[i]]:10}  {status[found[i]]:25}\n")
    elif searchType == "3": #exits program
        print("EXIT")
        answer = "x"
    else:
        print("\nINVALID ENTRY!!!") #if searchType input isnt 1-3
    if searchType == "1" or searchType == "2":  #allows user to keep using program and/or exit
        answer = input("Would you like to search again? [Y/N]: ").lower()

print("Thank you for using the Book Search Program! Have a Nice Day!")
#end