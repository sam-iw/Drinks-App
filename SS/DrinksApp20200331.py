import os
import csv
import datetime
import DrinksApp.persistence.save as persave
import DrinksApp.persistence.load as perload
import DrinksApp.persistence.print as perprint


os.system("Clear")

people = []
drinks = []
preferences = {}
new_round = {}
currentDT = datetime.datetime.now()

# Asks for user input which equals result, returns a string
def initial_options():
    os.system("Clear") #Remove / Refresh screen
    result = input("""Please. select option you would like to use:\n[1] People List\n[2] Drinks List\n[3] Add Person\n[4] Add Drink\n[5] Delete People\n[6] Delete Drinks\n[7] Choose Preferences\n[8] Print Function (menu)\n[9] Take Round (Under Construction)\n[10] Exit\nEnter Here: """)
    initial_function(result) #evokes the if function (menu) within the "Initial_Function"

# Defines what outcome is associated with each input from initial options
def initial_function(number):
    if number == "1":
        os.system("Clear")
        print("""These are the people on the app: """)
        perprint.print_list(people)
        nav_options()
    elif number == "2":
        os.system("Clear")
        print("""These are the drinks available on the app: """)
        perprint.print_list(drinks)
        nav_options()
    elif number == "3":
        os.system("Clear")
        type_entry(people)
        perprint.print_list(people)
        persave.save_list("persistence/people.txt", people)
    elif number == "4":
        os.system("Clear")
        type_entry(drinks)
        persave.save_list("persistence/drinks.txt", drinks)
        perprint.print_list(drinks)
    elif number == "5":
        os.system("Clear")
        delete_inputs(people)
        perprint.print_list(people)
    elif number == "6":
        os.system("Clear")
        delete_inputs(drinks)
        perprint.print_list(drinks)
    elif number == "7":
        os.system("Clear")
        add_preference(preferences)
        print(preferences)
        persave.save_csv_dictionary("persistence/preferences.csv", preferences)
        nav_options()
    elif number == "8":
        os.system("clear")
        print_functions()
        nav_options()
    elif number == "9":
        os.system("clear")
        print("Area currently down for maintenance due to developer incompetence")
        # brewer = input("Who would like to create a round? \nEnter Here: ")
        # new_round = Drinks_Preferences(brewer)
        # while True:
        #     drinker = input("""Add a drinker's name or hit enter to stop adding people: """)
        #     try:
        #         if drinker == "":
        #             break
        #         new_round.add_person(drinker)
        #     except:
        #         print("""I don't recognise that person, please enter their name and preference below: """)
        #         add_preference()
        #         new_round.add_person(drinker)
        # print(new_round.orders)
        # persave.save_dictionary("persistence/newround.txt", new_round.orders)
        nav_options()
    elif number == "10":
        os.system("Clear")
        print("Catch you later")
        persave.save_list("persistence/people.txt", people)
        persave.save_list("persistence/drinks.txt", drinks)
        exit()
    else:
        print("This is an invalid input")
        initial_options()



# Once operation is complete what will the user want to do next? (if function)
def nav_options():
    numbertwo = input("""Please select your next option:\n[1] Return to main menu\n[2] Exit the options\nEnter Here: """)
    if numbertwo == "1":
        persave.save_list("persistence/people.txt", people)
        persave.save_list("persistence/drinks.txt", drinks)
        initial_options()
    elif numbertwo == "2":
        os.system("Clear")
        print("Catch you later")
        persave.save_list("persistence/people.txt", people)
        persave.save_list("persistence/drinks.txt", drinks)
        exit()
    else:
        os.system("Clear")
        print("This is an invalid input, please re-select an option.")
        nav_options()


# Generic add entry to list function.
def type_entry(List):
    os.system("Clear")
    print("""The list below is what is currently stored in the app.""")
    perprint.print_list(List)
    Entries = input("Enter New Entry: ")
    for Entry in Entries.split(", "):
        List += [Entry]
        perprint.print_list(List)
        nav_options()


# Generic delete function that includes an exception rule.
def delete_inputs(List):
    os.system("Clear")
    print("Below is a list of items currently stored in the app, which would you like to delete?")
    perprint.print_list(List)
    Deletions = input ("Enter what to delete: ")
    try:
        for Deletion in Deletions.split(", "):
            List.remove(Deletion)
        print("The remaining items stored in the app are below:")
        perprint.print_list(List)
        nav_options()
    except:
        print("You have made an invalid entry.")
        nav_options()


def add_preference(dictionary):
    preference = input("""Add a person and preference in format of "person: drink": """)
    split_preference = preference.strip().split(": ")
    person = split_preference[0]
    drink = split_preference[1]
    dictionary[person] = drink
    return dictionary


# Which person should a drinks preference be assigned?
def choose_person():
    perprint.print_list(people)
    Person_Choice = input("Choose which person: ")
    print(f"You selected:  {Person_Choice}")
    return Person_Choice


# Which drink should be assigned to each of the
def choose_drink():
    perprint.print_list(drinks)
    Drinks_Choice = input("Choose which drink preference (only one drink per person): ")
    print(f"You selected: {Drinks_Choice}")
    return Drinks_Choice


def items_in_list(list):
    count = 1
    for item in list:
        print(f" | {count}. {item} |")
        count += 1


def print_functions():
    print_choice = input("""What would you like to print:\n[A] Print People\n[B] Print Drinks\n[C] Print Preferences\n[D] Print Round\n Enter Here: """)
    if print_choice == "A":
        os.system("Clear")
        perprint.print_list(people)
    elif print_choice == "B":
        os.system("Clear")
        perprint.print_list(drinks)
    elif print_choice == "C":
        os.system("Clear")
        print(" |  Preferences  |")
        count = 1
        for key, value in preferences.items():
            print(f" |  {count}. {key}'s drink of choice is {value}  |")
            count += 1
    elif print_choice == "D":
        os.system("Clear")
        print(" | Drinks Round |")
        count = 1
        for key, value in new_round.items():
            print(f" |  {count}. {key}'s would like a {value}  |")
            count += 1
    else:
        os.system("Clear")
        print("This is an invalid input")
        initial_options()


# This function generates the horizontal lines for the table
def outline():
    print("-" * 25)


def generate_table(Header, list):
    outline()
    print(f"| {Header.upper()}")
    outline()
    count = 1
    for item in list:
        print(f" | {count}. {item} |")
        count += 1
    outline()


def test_add_preference():
    # Arrange
    test_preferences = {}
    test_preference = "Alex: Wine"
    expected_outcome = {"Alex": "Wine"}

    # Act
    actual_outcome = add_preference(test_preference,test_preferences)

    # Assert
    assert actual_outcome == expected_outcome, f"""
    actual outcome = {actual_outcome}
    expected outcome = {expected_outcome}"""
    print("Passed the GDPR test")


if __name__ == "__main__":


    perload.load_dictionary("persistence/newround.txt", new_round)
    perload.load_csv_dictionary("persistence/preferences.csv", preferences)
    perload.load_lists("persistence/people.txt", people)
    perload.load_lists("persistence/drinks.txt", drinks)
    initial_options()

    SystemExit