#Keith Phaneuf
#SE126.04
#Lab 1
#1-9-2025 [W1D2]

#PROGRAM PROMPT:  
# You will be writing one Python file for this project- it is a program that determines whether a
# meeting room is in violation of fire regulations regarding the maximum room capacity. The
# program will accept the maximum room capacity and the number of people attending the
# meeting. If the number of people is less than or equal to the maximum room capacity, the
# program announces that it is legal to hold the meeting and tells how many additional people may
# legally attend. If the number of people exceeds the maximum room capacity, the program
# announces that the meeting cannot be held as planned due to the fire regulation and tells how
# many people must be excluded in order to meet the fire regulations. The user should be allowed
# to enter and check as many rooms as they would like without exiting the program.

#VARIABLE DICTIONARY
#max_room       the maximum capacity of the room
#people         the sum total of all temps entered
#response       a "y" or "n" answer as to if the user wants to use the program
#diff           the difference between max_room and people 
#allow          helps display difference between max_room and people

#FUNCTIONS
def decision(response): #function header
    '''this function asks a user if they'd like to enter another temp, checks the response for validility, and then returns a valid response back to the main program'''

    response = input("Would you like to test a room capacity? [y/n]").lower()

    #user error trap loop - ensures user provides valid value
    while response != "y" and response != "n":
        print("***INVALID ENTRY!***")
        response = input("Would you like to test a room capacity? [y/n]").lower()

    return response #this value will replace the function call in the main code

def difference(people, max_room): #when the capacity of the room is not met

    diff = max_room - people
    
    return diff #this value will replace the function call in the main code
def neg_difference(people, max_room): #for when there are too many people

    diff = people - max_room
    
    return diff #this value will replace the function call in the main code

#MAIN CODE

response = input("Press y to start: [y]").lower() #using to start program

while decision(response) == "y" and response == "y": #while loop for while user uses program for calculations
    response = "n"
    meeting_name = input("What is the name of the meeting? ")
    max_room = int(input("What is the maximum capacity of the room? "))
    people = int(input("How many people are attending the meeting? "))
    if people <= max_room: #if there are not too many people signed up for the meeting
        print("It is legal to hold the meeting in the room")
        allow = difference(people, max_room)
        print(f"{allow} person/people can be added to the meeting and still meet fire regulations. ")
        
    else: #if there are too many people signed up for the meeting
        print("The meeting can not be held as planned due to fire regulations!")
        allow = neg_difference(people, max_room)
        print(f"{allow} person/people must be removed from the meeting to meet fire regulations. ")
    response = "y" #helps keep code working properly

print("Have a great day!") #end message