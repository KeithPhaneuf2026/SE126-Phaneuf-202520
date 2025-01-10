#Keith Phaneuf
#SE126.04
#Lab 1
#1-9-2025 [W1D2]

#VARIABLE DICTIONARY
#max_room       the maximum capacity of the room
#people         the sum total of all temps entered
#difference     the amount of people you can add to the room and still be legal
#tempF          the temp in Fahrenheit, entered by the user
#tempC          the temp in Celsius (tempC = (tempF - 32) * (5 / 9))
#answer         loop control; value determines if loop repeats, entered by the user

#--------FUNCTIONS--------------------------------------------
def again(): #<--FUNCTION HEADER
    '''this function asks a user if they'd like to enter another temp, checks the response for validility, and then returns a valid response back to the main program'''

    ans = input("\t\tWould you like to test a room capacity? [y/n]").lower()

    #user error trap loop - ensures user provides valid value
    while ans != "y" and ans != "n":
        print("***INVALID ENTRY!***")
        ans = input("\t\tWould you like to test a room capacity? [y/n]").lower()

    return ans #this value will replace the function call in the main code

def difference(people, max_room):

    diff = max_room - people
    
    return diff

while again() == "y":
    max_room = int(input("What is the maximum capacity of the room?"))
    people = int(input("How many people are attending the meeting?"))
    if people <= max_room:
        print("It is legal to hold the meeting in the room")
        print("Amount of people you can add to the room and still abide by fire regulations: ")
        allow = difference(people, max_room)
        print(allow)
    else:
        print("The meeting can not be held as planned due to fire regulations!")
        print("Amount of people you need to remove from the meeting to abide by fire regulations: ")
        allow = difference(people, max_room)
        print(allow)