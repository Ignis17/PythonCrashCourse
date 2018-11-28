# Author: Joel Turbi
# Description: Creates a dictionary for seasons

def main():
    # Seasons dictionary.
    seasons = {"Spring": ["March", "April", "May", "June"],
            "Summer": ["June", "July", "Ausgust", "September"],
            "Fall": ["September", "October", "November", "December"],
            "Winter": ["December", "January", "February", "March"]}
    # Gets input from user.
    choice = input("Enter a season: ").title()
    # Will keep asking for input as long as input is not the input desired.
    while(True):
        if (choice not in seasons):
            print("Please, enter a valid season. e.g \"Summer\",etc.")
            choice = input("Enter a season: ").title()
        else:
            # Prints without brakets or commas, separating with "--"
            print(*seasons[choice], sep="--")
            return True


main()
