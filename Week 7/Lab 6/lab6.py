#Keith Phaneuf
#SE126.04
#Lab 6
#2-24-2025 [W8D1]

#PROGRAM PROMPT:
'''
For Lab #6, you must use lists to create the airplane seating chart - either 1D or 2D lists. You may either create a file to read the data in for the seats, or you can hand-populate your own 1/2D lists. If you choose to create your own file, please upload along with your completed Lab #6 .py file. 

Lab #6 is due by the end of class W8D1. 

Due to the 10week quarterly schedule, this is the last lab assignment that will remain open for late submissions with the full 2-week grace period window.
6. (Absolute C++, 3rd Edition. Savitch, Walter. P. 223 #10)
Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane.  Assume a small airplane with seat numbering as follows.
	
Row					
1	A	B		C	D
2	A	B		C	D
3	A	B		C	D
4	A	B		C	D
5	A	B		C	D
6	A	B		C	D
7	A	B		C	D

The program should display the seat pattern, with an ‘X’ making the seats already assigned. For example, after seats 1A, 2B and 4C are taken the display should look like this:

Row					
1	X	B		C	D
2	A	X		C	D
3	A	B		C	D
4	A	B		X	D
5	A	B		C	D
6	A	B		C	D
7	A	B		C	D

After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated.  This continues until all seats are filled or until the user signals that the program should end.  If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.
•	You must use a function to display the seating map
•	You must use a function that asks the user in they want to continue reserving seats or stop. The function should only accept an uppercase or lowercase ‘y’ or ‘n’.
'''


#functions
def display():#displays plane seats
    print("Row ------------------")
    for i in range(0, len(planeSeating)):
        print(f"{i + 1:3}   {planeSeating[i][0]:3} {planeSeating[i][1]:6} {planeSeating[i][2]:3} {planeSeating[i][3]:3}")

#lists
planeSeating = [
    ['A','B','C','D'],
    ['A','B','C','D'],
    ['A','B','C','D'],
    ['A','B','C','D'],
    ['A','B','C','D'],
    ['A','B','C','D'],
    ['A','B','C','D']
]

display()#displays starting list

reserve = "y"#automatically enters reserving program
while reserve == "y":
    userSeat = input("Please type in a seat number to reserve a seat [ex. 4B]: ").upper()#input for seat to be reserved
    
    #psychotic method of changing each item in list to 'X' for taken
    if userSeat == "1A":
        if planeSeating[0][0] == "X":#if spot already taken
            print("Spot already reserved!")
        else:#changes to X
            planeSeating[0][0] = "X"
            display()
    elif userSeat == "1B":
        if planeSeating[0][1] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[0][1] = "X"
            display()
    elif userSeat == "1D":
        if planeSeating[0][2] == "X":
            print("Spot already reserved!")
        else:     
            planeSeating[0][2] = "X"
            display()
    elif userSeat == "1D":
        if planeSeating[0][3] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[0][3] = "X"
            display()
    elif userSeat == "2A":
        if planeSeating[1][0] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[1][0] = "X"
            display()
    elif userSeat == "2B":
        if planeSeating[1][1] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[1][1] = "X"
            display()
    elif userSeat == "2C":
        if planeSeating[1][2] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[1][2] = "X"
            display()
    elif userSeat == "2D":
        if planeSeating[1][3] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[1][3] = "X"
            display()
    elif userSeat == "3A":
        if planeSeating[2][0] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[2][0] = "X"
            display()
    elif userSeat == "3B":
        if planeSeating[2][1] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[2][1] = "X"
            display()
    elif userSeat == "3C":
        if planeSeating[2][2] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[2][2] = "X"
            display()
    elif userSeat == "3D":
        if planeSeating[2][3] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[2][3] = "X"
            display()
    elif userSeat == "4A":
        if planeSeating[3][0] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[3][0] = "X"
            display()
    elif userSeat == "4B":
        if planeSeating[3][1] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[3][1] = "X"
            display()
    elif userSeat == "4C":
        if planeSeating[3][2] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[3][2] = "X"
            display()
    elif userSeat == "4D":
        if planeSeating[3][3] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[3][3] = "X"
            display()
    elif userSeat == "5A":
        if planeSeating[4][0] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[4][0] = "X"
            display()
    elif userSeat == "5B":
        if planeSeating[4][1] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[4][1] = "X"
            display()
    elif userSeat == "5C":
        if planeSeating[4][2] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[4][2] = "X"
            display()
    elif userSeat == "5D":
        if planeSeating[4][3] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[4][3] = "X"
            display()
    elif userSeat == "6A":
        if planeSeating[5][0] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[5][0] = "X"
            display()
    elif userSeat == "6B":
        if planeSeating[5][1] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[5][1] = "X"
            display()
    elif userSeat == "6C":
        if planeSeating[5][2] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[5][2] = "X"
            display()
    elif userSeat == "6D":
        if planeSeating[5][3] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[5][3] = "X"
            display()
    elif userSeat == "7A":
        if planeSeating[6][0] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[6][0] = "X"
            display()
    elif userSeat == "7B":
        if planeSeating[6][1] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[6][1] = "X"
            display()
    elif userSeat == "7C":
        if planeSeating[6][2] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[6][2] = "X"
            display()
    elif userSeat == "7D":
        if planeSeating[6][3] == "X":
            print("Spot already reserved!")
        else:
            planeSeating[6][3] = "X"
            display()
    else:
        #if input doesn't match available seat
        print("INVALID ENTRY: Watch casing and spelling")
    reserve = input("Would you like to reserve another seat? [y/n]")

display()#displays ending list