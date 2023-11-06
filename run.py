from dateutil.parser import parse
from datetime import datetime
from termcolor import colored
from pyfiglet import figlet_format
import random


def user_input():
    """
    Get input from user and to make sure user is making a valid 
    choice. The while loop will repeat and request data that is valid.
    The user can only enter a number.
    """
    while True:
        user_choice = (input("How many travelers are there? (1 if you are traveling alone, 2 or more for traveling with company:\n"))
        if user_choice.isdigit() >= 1:
            return int(user_choice)
        else:
            print(colored("Invalid choice. Please enter a valid number!", "red"))
            


def travel_date():
    """
    Get input from the user about travel date. A while loop that will repeat until a valid date is entered.
    The parse method is used to validate the date format.
    Dayfirst is used to validate that the user's input is a date in the future and not in the past.
    """
    while True:
        departure = input("When do you want to travel? (YYYY-MM-DD):\n")
        try:
            day_and_date = parse(departure, dayfirst=True)
            if parse(departure) >= day_and_date.today():
                print(day_and_date.strftime("%A"))
                return day_and_date
            else:
                print(colored("Please enter a valid date in YYYY-MM-DD format", "red"))
        except ValueError:
            print(colored("Please enter a valid date in YYYY-MM-DD format", "red"))
            
    

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
            print(colored("Invalid input. Please enter a number!", "red"))
           


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
        {"City": "Manilla", "Price": 700}, 
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
    ]
}



def continent():
    """
    Get user input. User needs to select a contintent to get a random city returned
    in the random_destination function.
    """
    while True:
        user_selection = input("Choose a continent (Africa, Asia, Europe, North America, South America): \n")
        if user_selection in random_city_dict:
            return user_selection
        else:
            print(colored("Invalid continent. Please choose from the continents listed", "red"))
           



def random_destination(user_selection):
    """
    Returns a random city and the price from the dictionary to the user. Based on the user input in the 
    continent function.
    """
    if user_selection in random_city_dict:
        random_city = random.choice(random_city_dict[user_selection])
        the_city = random_city["City"]
        the_price = random_city["Price"]

        print(f"Your Random destination is: \nCity: {the_city}")
        print(f"Price: {the_price}$")
        return the_city, the_price
    

def another_choice():
    new_choice = input("Do you want to choose another city?: (y/n)\n").upper()
    if new_choice == "y":
        return(continent())
    
      

def summary(user_choice, departure, travel_duration, the_city, the_price):
    print("Here is your travel information: \n")
    print(f"Traveling on: {departure}")
    print(f"Number of people traveling: {user_choice}")
    print(f"Duration of stay: {travel_duration} days")
    print(f"Destination: {the_city}")
    print(f"Total cost: ${the_price}")



def main():
    #Change the welcomes text font color and text to ascii art
    banner_text = "Welcome to the Random Destination\n Generator!"
    print(colored(figlet_format(banner_text, font="small"), color="cyan"))

    #Ascii art file to print airplane image
    airplane_file = "airplane.txt"

    try:
        with open(airplane_file, "r") as file:
            airplane = file.read()
            print(colored(airplane, color="green"))
    except FileNotFoundError:
        print("File not found")





    print("Get a random travel destination based on your choice of continent....let's begin! \n")
    
    user_choice = user_input()
    departure = travel_date()
    travel_duration = duration()
    user_selection = continent()
    random_destination(user_selection)
    new_choice = another_choice()
    the_city, the_price = random_destination(user_selection)
    summary(user_choice, departure, travel_duration, the_city, the_price)
    

   

main()
