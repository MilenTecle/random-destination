import gspread
from google.oauth2.service_account import Credentials
from dateutil.parser import parse
from datetime import datetime
from termcolor import colored
from pyfiglet import figlet_format
from tabulate import tabulate
import random

#Lists the API:s for access
#Code from my Love Sandwiches project
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('random-destination')

continents = SHEET.worksheet('continents')

data = continents.get_all_values()


def user_input():
    """
    Get input from user and to make sure user is making a valid 
    choice. The while loop will repeat and request data that is valid.
    The user can only enter a number starting from 1.
    """
    while True:
        user_choice = (input("  How many travelers are there? \n  (1 if you are traveling alone, 2 or more for traveling with company:\n\n  "))
        if user_choice.isdigit() and int(user_choice) > 0:
            return int(user_choice)
        else:
            print(colored("  Invalid choice. Please enter a valid number!", "red"))
            


def travel_date():
    """
    Get input from the user about travel date. A while loop that will repeat until a valid date is entered.
    The parse method is used to validate the date format.
    Dayfirst is used to validate that the user's input is a date in the future and not in the past.
    """
    while True:
        departure = input("  When do you want to travel? (YYYY-MM-DD):\n\n  ")
        try:
            day_and_date = parse(departure, dayfirst=True)
            if parse(departure) >= day_and_date.today():
                weekday = day_and_date.strftime("%A")
                print(f"  {weekday}\n")
                return day_and_date
            else:
                print(colored("  Please enter a valid date in YYYY-MM-DD format", "red"))
        except ValueError:
            print(colored("  Please enter a valid date in YYYY-MM-DD format", "red"))
            
    

def duration():
    """
    Get input from the user about the duration of the stay with
    validation to make sure the user only can type in numbers,
    starting from 1.
    """
    while True:
        travel_duration = (input("  How many days are you planning to stay?:\n\n  "))
        if travel_duration.isdigit() and int(travel_duration) > 0:
            return int(travel_duration)
        else:
            print(colored("  Invalid input. Please enter a number!", "red"))
           


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
        user_selection = input("  Choose a continent (Africa, Asia, Europe, North America, South America): \n\n  ")
        if user_selection in random_city_dict:
            return user_selection
        else:
            print(colored("  Invalid continent. Please choose from the continents listed", "red"))
           



def random_destination(user_selection):
    """
    Returns a random city and the price from the dictionary to the user. Based on the user input in the 
    continent function.
    """
    if user_selection in random_city_dict:
        random_city = random.choice(random_city_dict[user_selection])
        the_city = random_city["City"]
        the_price = random_city["Price"]

        print(f"  Your Random destination is: \n\n  City: {the_city}")
        print(f"  Price: {the_price}$\n"  )
        return the_city, the_price
    

def another_choice():
    while True:
        new_choice = input("  Do you want to choose another city?: (y/n)\n\n  ").lower()
        if new_choice == "y":
            return continent()
        elif new_choice == "n":
            break
        else:
            print("  Invalid choice. Please enter 'y' or 'n'")

def travel_package():
    while True:
        accomodation = input("  Do you want to add accomodation?: (y/n)\n\n  ").lower()
        if accomodation =="y":
            return accomodation_choices()
        elif accomodation == "n":
            break
        else:
            print("  Invalid choice. Please enter 'y' or 'n'")


def accomodation_choices():
    print("  Select an option for accomodation\n")
    print("  1. Luxury Hotel")
    print("  2. Budget Hotel")
    print("  3. Airbnb")
    print("  4. Hostel\n")
    
    option = input("  Enter the number of your choice\n  ")
    
    if option == "1":
        print("  Luxury Hotel\n"  )
    elif option == "2":
        print("  Budget Hotel\n"  )
    elif option == "3":
        print("  Airbnb\n  ")
    elif option == "4":
        print("  Hostel\n  ")
    else:
        print(colored("  Invalid choice. Please choose from the options provided,\n  ", "red"))
    



   
"""
Function to display a summary over the travel information, taking
the parameters all related to the travel info. From users input and the
random city generated. The summary will be displayed in a table using the tabulate module
"""
def summary(user_choice, departure, travel_duration, the_city, the_price):
    total_cost = user_choice * the_price
    travel_details = [
        ["Traveling on:", departure],
        ["Number of people traveling:", user_choice],
        ["Duration of stay:", f"{travel_duration} days"],
        ["Destination:", the_city],
        ["Total cost:", f"${total_cost}"],
    ]
    
    table_style = "grid"
    table = tabulate(travel_details, tablefmt=table_style)

    print("  Here is your travel information: \n")
    print(colored(table, color="light_blue"))

def main():
    """
    #Change the welcomes text font color and text to ascii art
    welcome = "Welcome"
    text = "to the Random Destination Generator!\n\n"
    print(colored(figlet_format(welcome, font="doom"), color="light_blue"))
    print(colored(text, "light_blue"))
"""
    
    #Ascii art file to print images

    welcome_text = "welcome.txt"
    airplane_file = "airplane.txt"

    #Prints welcome text
    try:
        with open(welcome_text, "r") as file:
            welcome = file.read()
            print(welcome)
    
    #Prints airplane image
        with open(airplane_file, "r") as file:
            airplane = file.read()
            print(colored(airplane, color="light_blue"))
            print("\n")
    except FileNotFoundError:
        print("  File not found")
        





    print("  Get a random travel destination based on your choice of continent.\n  Let's begin! \n")
    input("  Press any key to continue...\n  ")

    user_choice = user_input()
    departure = travel_date()
    travel_duration = duration()
    user_selection = continent()
    random_destination(user_selection)
    new_choice = another_choice()
    the_city, the_price = random_destination(user_selection)
    accomodation = travel_package()
    summary(user_choice, departure, travel_duration, the_city, the_price)
    

   

main()
