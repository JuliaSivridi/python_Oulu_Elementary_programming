"""
Defines the donkeygothi's user interface.
"""
import donkeydefs

def show_state(donkeydata):
    """
    Prints the donkey's current state (age, money, satiation, happiness, energy).
    If the donkey is retired, it prints a retirement message.
    """
    print(f"The donkey is {donkeydata['AGE']} years old and has {donkeydata['MONEY']} eur.")
    print(f"Satiation: {donkeydata['SATIATION']}")
    print(f"Happiness: {donkeydata['HAPPINESS']}")
    print(f"Energy: {donkeydata['ENERGY']}")
    
    if donkeydata["RETIRED"]:
        print("The donkey has retired.")

def prompt_choice(donkeydata):
    """
    Prompts the user for a choice and validates it based on the donkey's state.
    Returns a valid input made by the user (string).
    """
    if donkeydata["RETIRED"]:
        valid_choices = donkeydefs.RETIREMENT_CHOICES
    else:
        valid_choices = donkeydefs.CHOICES
    
    # Print available choices
    print(f"Choices: {', '.join(valid_choices)}")
    
    while True:
        choice = input("Input next choice: ").strip().lower()
        if choice in valid_choices:
            return choice
        print("Invalid input!")
