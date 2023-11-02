
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



#def travel_dates():



#def duration():


def main():
    print("Welcome to the Random Destination Generator!")



main()
