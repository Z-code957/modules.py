"""1.Number game
Outline:
Write a program to generate a random integer and match it with the input given by the user?
Project:
https://replit.com/~
2.Rock paper scissors
Outline:
Create a program to play rock, paper, and scissors. Use a random module to select from the given options Check whether the random guess matches the user’s answer
Project:
https://replit.com/~
3.Mathematical operations
Outline:
Write a program to understand the different functions of the math module.
Project:
https://replit.com/~"""

"""import random
integer = int(input("Enter any number between the range of 1 to 3: "))
r = random.randint(1,3)
while True:
    if integer == r:
        print("Both numbers are same.",integer)
        break
    else:
        print("Wrong number.",r)
        break"""

"""import random
options=["rock","paper","scissor"]
computer = random.choice(options)
print("computer choice is ",computer)
user=input("Choose between rock, paper, scissor: ")
print("User choice is",user)
if user==computer:
    print("ITS A TIE")
elif user=="rock" and computer=="scissor":
    print("ROCK SMASHES SCISSORS,YOU WIN")
elif user=="paper" and computer=="rock":
    print("paper covers rock,YOU WIN")
elif user=="scissor" and computer=="paper":
    print("scissor cuts paper,YOU WIN")
else:
    print("you lost")"""

import math
print(math.ceil(5.3))
print(math.floor(5.3))
print(math.exp(5))