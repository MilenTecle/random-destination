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


#print(f"Travel duration: {travel_duration} days")

#A dictionary with keys and lists of tuples to be used to return a random city to the user
random_city_dict= {
"Africa": [("Cairo, $450"), ("Addis Abeba, $750"), ("Cape Town, $800"), ("Stone Town, $800"), ("Casablanca, $450")],
"Asia": [("Tokyo, $750"), ("Manilla, $700"), ("Hanoi, $730"), ("Singapore, $680"), ("Seoul, $760")],
"Europe": [("Rome, $300"), ("Madrid, $350"), ("London, $380"), ("Athens, $400"), ("Berlin, $280")],
"North America": [("Santo Domingo, $650"), ("Mexico City, $450"), ("New York City, $500"), ("Calgary, $580"), ("Havana, $620")],
"South America": [("Rio de Janerio, $700"), ("Buenos Aires, $800"), ("Lima, $850"), ("Bogotá, $750"), ("Caracas, $780")],
}



def continent():
    """
    Get user input. User needs to select a contintent to get a random city returned
    """
    while True:
        user_selection = input("Choose a contintinent (Africa, Asia, Europe, North America, South America): \n")
        if user_selection in random_city_dict:
            return user_selection
        else:
            print("Invalid continent. Please choose from the continents listed")


def main():
    print("Welcome to the Random Destination Generator! \n")
    print("Get a random travel destination based on you choice of continent....let's begin! \n")
    
    user_choice = user_input()
    departure = travel_date()
    travel_duration = duration()
    user_selection = continent()

   

main()
