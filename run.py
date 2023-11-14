import gspread
from google.oauth2.service_account import Credentials
from dateutil.parser import parse
from datetime import datetime
from termcolor import colored
from pyfiglet import figlet_format
from tabulate import tabulate
import random
import os
from time import sleep
from PIL import Image

"""
image_file = 'image.jpg'
image = Image.open(image_file)
image.show()
"""

# Lists the API:s for access
# Code from my Love Sandwiches project

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('random-destination')


def user_input():
    """
    Get input from user and to make sure user is making a valid
    choice. The while loop will repeat and request data that is valid.
    The user can only enter a number starting from 1.
    """
    while True:
        user_choice = (input("  How many travelers are there?: \n  "
                             "(1 if you are traveling alone, 2 or"
                             " more for traveling with company)\n\n  "))
        if user_choice.isdigit() and int(user_choice) > 0:
            return int(user_choice)
        else:
            print(colored(
                "  Invalid choice. Please enter a valid number.", "red"))


def travel_date():
    """
    Get input from the user about travel date. A while loop
    that will repeat until a valid date format is entered.
    The datetime.strptime will parse the date. By using datetime.now.date
    it will then check and validate that the user's
    input is a date in the future and not in the past.
    The weekday correspeonding to the date will also be printed.
    """
    while True:
        departure = input("  When do you want to travel? (YYYY-MM-DD):\n\n  ")
        try:
            day_and_date = datetime.strptime(departure, "%Y-%m-%d")
            if day_and_date.date() >= datetime.now().date():
                weekday = day_and_date.strftime("%A")
                print(f"  {weekday}\n")
                return day_and_date, weekday
                print("\n")
            else:
                print(colored(
                    "  Please enter a valid date in YYYY-MM-DD format", "red"))
        except ValueError:
            print(colored(
                "  Please enter a valid date in YYYY-MM-DD format", "red"))


def duration():
    """
    Get input from the user about the duration of the stay with
    validation to make sure the user only can type in numbers,
    starting from 1.
    """
    while True:
        travel_duration = (input("  How many days are you planning"
                                 " to stay?:\n\n  "))
        if travel_duration.isdigit() and int(travel_duration) > 0:
            return int(travel_duration)
            print("\n")
        else:
            print(colored("  Invalid input. Please enter a number", "red"))


def continent():
    """
    Get user input. User needs to select a contintent to get
    a random city returned in the random_destination function.
    The continents are each linked to a city and price in
    google sheets. Here it will access the worksheet for the
    chosen continent.
    """
    while True:
        user_selection = input("  Choose a continent (Africa, Asia, Europe,"
                               " North America, South America): \n\n"
                               "  ").lower()
        try:
            SHEET.worksheet(user_selection)
            return user_selection
            print("\n")
        except gspread.exceptions.WorksheetNotFound:
            print(colored(
                "  Invalid continent. Please choose from the "
                "continents listed", "red"))


def random_destination(user_selection):
    """
    Returns a random city and the price from the the list of citys
    from the google worksheet to the user.
    Based on the user input in the continent
    function it will access the worksheet. It will
    then get all the rows from the worksheet,
    choose a random city and print the random city and price.
    """
    try:
        worksheet = SHEET.worksheet(user_selection)
        data = worksheet.get_all_records()
        random_city = random.choice(data)
        the_city = random_city["City"]
        the_price = random_city["Price"]

        print("  Your Random destination is: \n  ")
        print(f"  City: {the_city}")
        print(f"  Price: {the_price}$\n")
        return the_city, the_price
    except gspread.exceptions.WorksheetNotFound:
        print("No city found")


def another_choice(user_selection):
    """
    Get user input if user wants to get another city chosen.
    A while loop that will display the continent function if user
    chooses 'y' and break the loop if user chooses 'n'. Will then
    proceed to next function.If neither y och n is entered a print
    message will display to promt the user to make a choice.
    """
    while True:
        new_choice = input("  Do you want to choose another city?:"
                           " (Y/N)\n\n  ").upper()
        if new_choice == "Y":
            user_selection = continent()
            the_city, the_price = random_destination(user_selection)
            return the_city, the_price
        elif new_choice == "N":
            return None
        else:
            print(colored("  Invalid choice. Please enter 'Y' or 'N'", "red"))


def travel_package():
    """
    Get user input if user wants to add accommodation. A while loop will run
    until a valid choice is made ('y' or 'n').
    If 'y' the accommodation function is called. If 'n' the loop will break.
    If neither y och n is entered, a print message will display to promt the
    user to make a choice.
    """
    while True:
        accommodation = input("  Do you want to add accommodation?: "
                              "(Y/N)\n\n  ").upper()
        if accommodation == "Y":
            return accommodation_choices()
        elif accommodation == "N":
            break
        else:
            print(colored("  Invalid choice. Please enter 'Y' or 'N'", "red"))


def accommodation_choices():
    """
    Prints out the choices for accommodation to the user and user can enter a
    number. If statements to return the correct value based on users choice.
    And validation if neither of the provided numbers are entered by the user.
    The transportation_service function is then called to proceed.
    """
    print("  Select an option for accommodation\n")
    print("  1. Luxury Hotel")
    print("  2. Budget Hotel")
    print("  3. Airbnb")
    print("  4. Hostel\n")

    option = input("  Enter the number of your choice\n  ")

    if option == "1":
        print("  Luxury Hotel\n")
        return "  Luxury Hotel\n  "
    elif option == "2":
        print("  Budget Hotel\n")
        return "  Budget Hotel\n  "
    elif option == "3":
        print("  Airbnb\n")
        return "  Airbnb\n  "
    elif option == "4":
        print("  Hostel\n")
        return "  Hostel\n  "
    else:
        print(colored(
            "  Invalid choice. Please choose from the options "
            "provided\n  ", "red"))
        sleep(2)
        return accommodation_choices()


def transportation_service():
    """
    Get user input if the user wished to add transportation services.
    A while loop will run until a valid choice is made ('y' or 'n'). If
    'y' the transportation_options function is called.
    If 'n' the loop will break. If neither y och n is entered,
    a print message will display to promt the user to make a choice.
    """
    while True:
        transportation = input("  Do you want to add transportation?: "
                               "(Y/N)\n\n  ").upper()
        if transportation == "Y":
            return transportation_options()
        elif transportation == "N":
            break
        else:
            print(colored("  Invalid choice. Please enter 'Y' or 'N'", "red"))


def transportation_options():
    """
    The options for transportation that will be displayed to the user.
    The choice will be printed out and the user has to type a valid number.
    """
    print("  Select an option for transportation\n  ")
    print("  1. Airport taxi")
    print("  2. Car rental")
    print("  3. Bus transfer\n ")

    selection = input("  Enter the number of your choice\n  ")

    if selection == "1":
        print("  Airport taxi\n ")
        return "  Airport taxi\n "
    elif selection == "2":
        print("  Car rental\n ")
        return "  Car rental\n "
    elif selection == "3":
        print("  Bus transfer\n ")
        return "  Bus transfer\n "
    else:
        print(colored(
            "  Invalid choice. Please choose from the options "
            "provided\n  ", "red"))
        sleep(2)
        return transportation_options()


"""
Function to display a summary over the travel information, taking
the parameters all related to the travel info. From users input and the
random city generated. The summary will be displayed in a table using the
tabulate module.
"""


def summary(user_choice, departure, travel_duration, the_city, the_price,
            option, selection):

    total_cost = user_choice * the_price
    departure, weekday = departure

    travel_details = [
        ["Traveling on:", f"{weekday}, {departure.strftime("%Y-%m-%d")}"],
        ["Number of people traveling:", user_choice],
        ["Duration of stay:", f"{travel_duration} days"],
        ["Destination:", the_city],
        ["Price:", f"${total_cost}"],
    ]

    """
    This will append the accommodation choice and transportation choice to
    the travel details table if the user makes a choice.
    """
    if option:
        travel_details.append(["Accommodation:", option])

    if selection:
        travel_details.append(["Transportation:", selection])

    # Displays the travel details in a table
    table_style = "grid"
    table = tabulate(travel_details, tablefmt=table_style)

    print("  Here is your travel information: \n")
    print(colored(table, color="yellow", attrs=["reverse", "bold"]))
    print("  \n")


def final_step():
    """
    Let's the user choose to start over or exit the program. If the user want
    to start over, the main function is called. If the user wants to exit the
    terminal is cleared and a print message is displayed.
    """
    print("  What do you want to do next?:\n  ")
    print("  1. Start over")
    print("  2. Exit")

    next = input("  Enter the number of your choice\n  ")

    if next == "1":
        print("  Okay...let's start from the beginning!\n ")
        return main()
    elif next == "2":
        os.system('clear')
        print("  Have a nice trip!\n ")
    else:
        print(colored(
            "  Invalid choice. Please choose from the options"
            "  provided\n  ", "red"))


def main():
    """
    Ascii art files do display the welcome text and the airplane.
    The files are openend and read, and if there is an error a print message
    will be displayed in the exception.
    """
    # Ascii art files to print images
    welcome_text = "welcome.txt"
    airplane_file = "airplane.txt"

    # Prints welcome text
    try:
        with open(welcome_text, "r") as file:
            welcome = file.read()
            print(welcome)

    # Prints airplane image
        with open(airplane_file, "r") as file:
            airplane = file.read()
            print(colored(airplane, color="light_blue"))
            print("\n")
    except FileNotFoundError:
        print("  File not found")

    """
    A welcome message followed with an input that will prompt the user to
    start the program. The input message will display after 1.5 seconds.
    """
    print("  Get a random travel destination based on your choice of "
          "continent.\n  ...Let's begin! \n")
    sleep(1.5)
    input("  Press Enter to continue...\n\n  ")

    """
    The functions below are called in the right order to display information
    to the user and get the input from the user
    """

    user_choice = user_input()
    departure = travel_date()
    travel_duration = duration()
    user_selection = continent()
    the_city, the_price = random_destination(user_selection)
    another_choice_input = another_choice(user_selection)
    if another_choice_input is not None:
        the_city, the_price = another_choice_input
    new_choice = another_choice(user_selection)
    accommodation = travel_package()
    transportation = transportation_service()
    summary(user_choice, departure, travel_duration, the_city, the_price,
            accommodation, transportation)
    next = final_step()


main()
