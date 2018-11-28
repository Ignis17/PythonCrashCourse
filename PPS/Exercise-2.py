# Author: Joel Turbi
# Description: Lottery Game

# Imports random number library
import random

# Checks if numbner is not in winning list
def Check(usernumbers, winningnumbers):
    for pick in usernumbers:
        if pick not in winningnumbers:
            return False
    return True

# Pick5 Lottery initialization
def Pick5():
    # Declared empty user number list.
    usernumbers = []
    # Initialized random winning numbers.
    winningnumbers = [random.randint(1, 44) for i in range(5)]

    # Asks user to enter 5 numbers from 1 to 44 and in inserts it into empty
    # list by its assigned index number.
    print("Please pick five numbers between 1 and 44:")
    usernumbers.insert(0, int(input("Enter your 1st #: ")))
    usernumbers.insert(1, int(input("Enter your 2nd #: ")))
    usernumbers.insert(2, int(input("Enter your 3rd #: ")))
    usernumbers.insert(3, int(input("Enter your 4th #: ")))
    usernumbers.insert(4, int(input("Enter your 5th #: ")))

    # Checks if winning numbers exist
    if(Check(usernumbers, winningnumbers) is True):
        print("\nThe winning numbers are:", *winningnumbers, sep=' ')
        print("CONGRATULATIONS! YOU WON THE LOTTERY!")
    else:
        print("\nThe winning numbers are:", *winningnumbers, sep=' ')
        print("Sorry, you do not win this time.")

# Definition: Main funtion.
def main():
    print("\t*** Welcome to PICK5 Lottery Game ***\n")
    Pick5()

# Calls main() function
main()
