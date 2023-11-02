import datetime
import random


def user_input():
    """
    Get input from user and to make sure user is making a valid 
    choice. The while loop will repeat and request data that is valid
    """
    while True:
        user_choice = input("Are you traveling alone or with company? (alone/with company):\n")
        if user_choice == "alone":
            return "alone"
        elif choice == "with company":
            return "with company"
        else:
            print("Invalid choice. Please choose 'alone' or 'with company'.")



def travel_date():
    """
    Get input from the user about travel date
    """
    departure = input("When do you want to travel? (MM/DD/YYY):\n")
    return departure




#def duration():


def main():
    print("Welcome to the Random Destination Generator!")
    
    user_choice = user_input()
    departure = travel_date()



main()
