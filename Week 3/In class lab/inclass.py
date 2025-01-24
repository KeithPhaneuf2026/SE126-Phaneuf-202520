#Keith Phaneuf
#SE126.04
#Lab 2
#1-23-2025 [W3D2]

#PROGRAM PROMPT:  
#Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.


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
#old_desktop    counts how many desktops are 2016 and older and need to be replaced
#old_laptop    counts how many laptops are 2016 and older and need to be replaced

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
#prints heading
print(f"\n\n{'Type':20}     {'Brand':5}               {'CPU':5}   {'RAM':5}   {'1st Disk':5}    {'No HDD':5}      {'2nd Disk':5}   {'OS':5}     {'YR':5}") #header
print("-------------------------------------------------------------------------------------------------------------------------------")
with open("Week 3/In class lab/filehandling-1.csv") as csvfile: #file
    file = csv.reader(csvfile)
    for rec in file:

        total_rec += 1
        if rec[0] == "L": #converts values to be more readable
            rec[0] = "Laptop"
        else:
            rec[0] = "Desktop"
        if rec[1] == "DL": #converts values to be more readable
            rec[1] = "Dell"
        elif rec[1] == "HP":#converts values to be more readable
            rec[1] = "Hewlett Packard"
        elif rec[1] == "GW":#converts values to be more readable
            rec[1] = "Gateway"
        #append statements add data to the empty lists
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

#counters for computers that need to be replaced
old_desktop = 0
old_laptop = 0

for i in range(0, len(yr)):
    #counts how many desktops and laptops need to be replaced

    if int(yr[i]) <= 16: #too outdated
        if type[i] == "Desktop":
            old_desktop += 1
        else:
            old_laptop += 1 #if not a desktop, it is a laptop and the laptop counter increases
#print statements below display how many computers need to be replaced, the cost of replacement, and the total amount of computers in the file. 
print(f"\nTotal amount of desktops that need to be replaced: {old_desktop} Cost: ${old_desktop * 2000:.2f}")
print(f"\nTotal amount of laptops that need to be replaced: {old_laptop} Cost: ${old_laptop * 1500:.2f}")
print(f"\nTotal Computers in the file: {total_rec}") #displays total amount of computers
