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

#imports
import csv

#lists
libraryNumber = []
title = []
author = []
genre = []
pageCount = []
status = []

#connected
totalRecords = 0

#prints header
print(f"{'TITLE':25}  {'Author':15}  {'GENRE':15}  {'PAGES':10}  {'STATUS':25}")
print("----------------------------------------------------------------------------------")

with open ("Week 6/Lab #5/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        totalRecords += 1
        libraryNumber.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        pageCount.append(rec[4])
        status.append(rec[5])
