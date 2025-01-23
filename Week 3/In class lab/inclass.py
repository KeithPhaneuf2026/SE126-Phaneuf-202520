#Keith Phaneuf
#SE126.04
#Lab 2
#1-23-2025 [W3D2]

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

#creates an empty list for every potential field
type = []
brand = []
cpu = []
ram = []
first_disk = []
no_hdd = []
second_disk = []
os = []
yr = []
print(f"\n\n{'Type':20}     {'Brand':5}               {'CPU':5}   {'RAM':5}   {'1st Disk':5}    {'No HDD':5}      {'2nd Disk':5}   {'OS':5}     {'YR':5}") #header
print("-------------------------------------------------------------------------------------------------------------------------------")
with open("Week 3/In class lab/filehandling-1.csv") as csvfile: 
    file = csv.reader(csvfile)
    for rec in file:

        total_rec += 1
        if rec[0] == "L": #converts values to be more readable
            rec[0] = "Laptop"
        else:
            rec[0] = "Desktop"
        if (brand == "DL"):#converts values to be more readable
            brand.append("Dell")
        elif (brand == "HP"):#converts values to be more readable
            brand.append("Hewlett Packard")
        elif (brand == "GW"):#converts values to be more readable
            brand.append("Gateway")
        type.append(rec[0])
        brand.append(rec[1])
        cpu.append(rec[2])
        ram.append(rec[3])
        first_disk.append(rec[4])
        no_hdd.append(rec[5])
        if int(rec[5]) == 1:
            second_disk.append("-----")
            os.append(rec[6])
            yr.append(rec[7])
        elif int(rec[5]) == 2:
            second_disk.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])

for index in range(0, len(type)):
    #for every item, index will start at 0 and run up to (not including) the length (# of items)
 
    print(f"{type[index]:20}     {brand[index]:18}  {cpu[index]:5}   {ram[index]:5}   {first_disk[index]:5}   {no_hdd[index]:5}           {second_disk[index]:5}      {os[index]:5}     {yr[index]:5}") #displays data
print(f"Total Computers in the file: {total_rec}") #displays total amount of computers