# Python Libraries
import random

# Declared empty string variables.
answer=""
guess=""

# Randomizes number from 1 to 100
num = random.randint(1,100)

guess = int(input("\nI'm thinking of a number! Try to guess the number I'm thinking of: "))
while(answer != "no"):
    if(num == guess):
        answer = input("\nThat's it! Would you like to play again? (yes/no) ")
        if(answer == "yes"):
            num = random.randint(1,100)
            guess = int(input("\nI'm thinking of a number! Try to guess the number I'm thinking of: "))
        elif(answer == "no"):
            print("Thanks for playing!")
        else:
            print("Invalid answer, try again.")
    elif(guess < num):
        guess = int(input("Too low! Guess again: "))
    elif(guess > num):
        guess = int(input("Too high! Guess again: "))
