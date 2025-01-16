#Keith Phaneuf
#SE126.04
#Lab 2
#1-16-2025 [W2D2]

#PROGRAM PROMPT:  
# You have been asked to produce a report that lists all the computers in the csv file filehandling.csv. 
# Your report should look like the following sample output.  
# The last line should print the number of computers in the file.


#VARIABLE DICTIONARY
#total_rec      total number of computers
#type           type of computer
#brand          brand of computer
#cpu            processor of computet
#ram            ammount of ram in computer
#first_disk     main drive
#no_hdd         number of disks
#second_disk    if the computer has an extra drive
#os             operating system
#yr             year computer was made

#Imports
import csv

#Connected to file
total_rec = 0 #used to count computers

print(f"\n\n{'Type':20}     {'Brand':5}               {'CPU':5}   {'RAM':5}   {'1st Disk':5}    {'No HDD':5}      {'2nd Disk':5}   {'OS':5}     {'YR':5}") #header
print("-------------------------------------------------------------------------------------------------------------------------------")
with open("Week 2/Lab #2/filehandling.csv") as csvfile: 
    file = csv.reader(csvfile)
    for rec in file:
        #each var is for a row in file
        type =          rec[0]
        brand =         rec[1]
        cpu =           rec[2]
        ram =           rec[3]
        first_disk =    rec[4]
        no_hdd =        int(rec[5])
        if (no_hdd == 1): #if there is an extra drive or not
            second_disk = "-----"
            os = rec[6]
            yr = rec[7]
        elif no_hdd == 2:
            second_disk = rec[6]
            os = rec[7]
            yr = rec[8]
        if (type == "L"): #converts values to be more readable
            type = "Laptop"
        else:
            type = "Desktop"
        if (brand == "DL"):#converts values to be more readable
            brand = "Dell"
        if (brand == "HP"):#converts values to be more readable
            brand = "Hewlett Packard"
        if (brand == "GW"):#converts values to be more readable
            brand = "Gateway"
        total_rec += 1 #adds to total number of computers

        print(f"{type:20}     {brand:18}  {cpu:5}   {ram:5}   {first_disk:5}   {no_hdd:5}           {second_disk:5}      {os:5}     {yr:5}") #displays data
    print(f"Total Computers in the file: {total_rec}") #displays total amount of computers