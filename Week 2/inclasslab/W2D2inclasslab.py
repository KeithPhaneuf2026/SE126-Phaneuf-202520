#w2D2 - Text File Handling Review

#Program Prompt:


#Variable Dictionary


#--Imports
import csv
#--Functions
def difference(people, max_cap):
    '''This function is passed two values and returns the difference between them'''
    diff = max_cap - people
    return diff #this value will replace the difference() call in the main code

#--Main Executing Code

#Initializing needed counting varialbes
total_rec = 0
rooms_over = 0

# connected to file
print(f"\n\n{'NAME':20}     {'MAX':5}   {'PPL':5}   {'OVER':5}")
print("---------------------------------------------------------")
with open("Week 2/inclasslab/classLab2.csv") as csvfile:
    #we must indent one level while connected to the file
    file = csv.reader(csvfile)
    for rec in file:
        #below code occurs for every record (row) in the file (text file -> 2D list!)
        #assign each field data value to a friendly variable name
        name = rec[0]
        max = int(rec[1])   #all text data is read as a string, so cast as a num!
        ppl = int(rec[2])
        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        #count and siplay the rooms that are over capacity (remaining is negative)
        if remaining < 0 :
            rooms_over += 1
            print(f"{name:20}   {max:5}   {ppl:5}   {remaining * -1:5}")

        #count all rooms
        total_rec += 1
# disconnected from file
#display final data (counting vars)
print(f"\nRooms currently OVER capacity: {rooms_over}")
print(f"Total rooms in the file: {total_rec}")