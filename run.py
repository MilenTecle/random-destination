from  datetime import datetime
import random


def user_input():
    """
    Get input from user and to make sure user is making a valid 
    choice. The while loop will repeat and request data that is valid
    """
    while True:
        user_choice = input("Are you traveling alone or with company? (alone/with company):\n").strip()
        if user_choice == "alone":
            return "alone"
        elif user_choice == "with company":
            return "with company"
        else:
            print("Invalid choice. Please enter 'alone' or 'with company'.")



def travel_date():
    """
    Get input from the user about travel date
    """
    while True:
        departure = input("When do you want to travel? (YYYY-MM-DD):\n")
        try:
            day_and_date = f"{datetime.now().strftime('%A')}, {datetime.now().date().strftime('%Y-%M-%D')}"
            return day_and_date
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format")
    


def duration():
    """
    Get input from the user about the duration of the stay
    """
    while True:
        travel_duration = (input("How many days are you planning to stay?:\n"))
        if travel_duration.isdigit():
            return int(travel_duration)
        else:
            print("Invalid input. Please enter a number!")


def main():
    print("Welcome to the Random Destination Generator!")
    
    user_choice = user_input()
    departure = travel_date()
    travel_duration = duration()



main()
