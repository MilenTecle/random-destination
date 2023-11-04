from dateutil.parser import parse
from datetime import datetime
import random


def user_input():
    """
    Get input from user and to make sure user is making a valid 
    choice. The while loop will repeat and request data that is valid.
    The user can only enter a number.
    """
    while True:
        user_choice = (input("How many travelers are there? (1 if you are traveling alone, 2 or more for traveling with company:\n"))
        if user_choice.isdigit() == 1:
            return int(user_choice)
        elif user_choice.isdigit() >= 2:
            return int(user_choice)
        else:
            print("Invalid choice. Please enter a valid number!")



def travel_date():
    """
    Get input from the user about travel date
    """
    while True:
        departure = input("When do you want to travel? (YYYY-MM-DD):\n")
        try:
            day_and_date = parse(departure)
            return day_and_date
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format")
    


def duration():
    """
    Get input from the user about the duration of the stay with
    validation to make sure the user only can type in numbers.
    """
    while True:
        travel_duration = (input("How many days are you planning to stay?:\n"))
        if travel_duration.isdigit():
            return int(travel_duration)
        else:
            print("Invalid input. Please enter a number!")


#print(f"Travel duration: {travel_duration} days")

#A dictionary of lists for each continent to return a random city to the user
random_city_dict= {
"Africa": [
{"City": "Cairo", "Price": 450}, 
{"City": "Addis Abeba", "Price": 750}, 
{"City": "Cape Town", "Price": 800},
{"City": "Stone Town", "Price": 800}, 
{"City": "Casablanca", "Price": 450}
],

"Asia": [
{"City": "Tokyo", "Price": 750}, 
{"City": "Manilla", "Price" 700}, 
{"City": "Hanoi", "Price": 730}, 
{"City": "Singapore", "Price": 680}, 
{"City": "Seoul", "Price": 760}

],
"Europe": [
{"City": "Rome", "Price": 300}, 
{"City": "Madrid", "Price": 350}, 
{"City": "London", "Price": 380}, 
{"City": "Athens", "Price": 400}, 
{"City": "Berlin", "Price": 280}

],
"North America": [
{"City": "Santo Domingo", "Price": 650}, 
{"City": "Mexico City", "Price": 450}, 
{"City": "New York City", "Price": 500}, 
{"City": "Calgary", "Price": 580}, 
{"City": "Havana", "Price": 620}

],
"South America": [
{"City": "Rio de Janerio", "Price": 700}, 
{"City": "Buenos Aires", "Price": 800}, 
{"City": "Lima", "Price": 850}, 
{"City": "Bogotá", "Price": 750}, 
{"City": "Caracas", "Price": 780},
}



def continent():
    """
    Get user input. User needs to select a contintent to get a random city returned
    """
    while True:
        user_selection = input("Choose a continent (Africa, Asia, Europe, North America, South America): \n")
        if user_selection in random_city_dict:
            return user_selection
        else:
            print("Invalid continent. Please choose from the continents listed")



"""def random_destination(user_selection):
    
  Returns a random city from the dictionaryto the user. Based on the user input in the 
    continent function.

    if user_selection in random_city_dict:
        return random[]
"""

def main():
    print("Welcome to the Random Destination Generator! \n")
    print("Get a random travel destination based on your choice of continent....let's begin! \n")
    
    user_choice = user_input()
    departure = travel_date()
    travel_duration = duration()
    user_selection = continent()

   

main()
