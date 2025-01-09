#Keith Phaneuf
#SE126.04
#Lab 1
#1-9-2025 [W1D2]

#VARIABLE DICTIONARY
#roomMax        the maximum capacity of the room
#peopleInRoom   the sum total of all temps entered
#extraPeople    the amount of people you can add to the room and still be legal
#tempF          the temp in Fahrenheit, entered by the user
#tempC          the temp in Celsius (tempC = (tempF - 32) * (5 / 9))
#answer         loop control; value determines if loop repeats, entered by the user

roomMax = int(input("What is the maximum capacity of the room?"))
peopleInRoom = int(input("How many people are attending the meeting?"))

if peopleInRoom <= roomMax:
    print("It is legal to hold the meeting in the room")
    extraPeople = roomMax - peopleInRoom
    print("Amount of people you can add to the room and still abide by fire regulations")