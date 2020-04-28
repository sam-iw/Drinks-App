import os
import datetime
import persistence.save as persave
import persistence.load as perload
import persistence.print as perprint
import persistence.roundclass as perround
import persistence.database as perdb


os.system("Clear")

people = []
hot_drinks = []
soft_drinks = []
alcoholic_drinks = []
hot_drinks_pref = {}
soft_drinks_pref = {}
alcoholic_drinks_pref = {}
new_round = {}
currentDT = datetime.datetime.now()
time = currentDT.strftime("%H:%M")


# Asks for user input which equals result, returns a string
def initial_options():
    os.system("Clear") # Remove / Refresh screen
    print("Welcome to the BrIW app")
    result = input("""Please select which option you would like to use:\n[1] Search People List\n[2] Search Drinks List\n[3] Add Person\n[4] Add Drink\n[5] Delete Person\n[6] Delete Drinks\n[7] Choose Preferences\n[8] Print Function (menu)\n[9] Take Round\n[10] Exit App \nEnter Here: """)
    initial_function(result)# evokes the if function (menu) within the "Initial_Function"


def initial_function(number): # Defines what outcome is associated with each input from initial options
    if number == "1": # Search person
        os.system("Clear")
        s1_search_people()
    elif number == "2": # Search drinks
        os.system("Clear")
        s2_search_drinks()
    elif number == "3": # Create Person
        os.system("Clear")
        s3_create_person()
    elif number == "4": # Create Drink
        os.system("Clear")
        s4_add_drinks()
    elif number == "5": # Delete Person
        os.system("Clear")
        s5_delete_person()
    elif number == "6": # Delete Drinks
        os.system("Clear")
        s6_delete_drinks_type()
    elif number == "7": # Choose Drinks Prefs
        os.system("Clear")
        s7_drinks_pref_menu()
    elif number == "8":
        os.system("clear")
        s8_print_functions()
    elif number == "9":
        os.system("clear")
        s9_round_type()
    elif number == "10":
        os.system("Clear")
        print("Catch you later")
        exit()
    else:
        print("This is an invalid input, what would you like to do?")
        initial_options()


def sn_nav_options(): # Once operation is complete what will the user want to do next? (if function)
    numbertwo = input("""\nPlease select your next option:\n[1] Return to main menu\n[2] Exit the app\nEnter Here: """)
    if numbertwo == "1":
        initial_options()
    elif numbertwo == "2":
        os.system("Clear")
        print("Catch you later")
        exit()
    else:
        os.system("Clear")
        print("This is an invalid input, please re-select an option.")
        sn_nav_options()


def s1_search_people():
    people = perdb.load_tables("people")
    search_entry = str(input(f"\nWho would you like to search for? Enter first name, surname or age. "
                             f"(Hit ENTER to quit), \nEnter here: ").capitalize())
    for person in people:
        if search_entry == "":
            break
        elif search_entry in (person.first_name, person.surname, person.age):
            print(f"{person.first_name} {person.surname}, {person.age}")
        else:
            continue
    not_found = input(f"Did the find who you were after? if not press A to add a new person (Hit ENTER to quit)"
                      f"\nEnter here: ")
    if not_found == "A":
        s3_create_person()
    else:
        sn_nav_options()


def s2_search_drinks():
    drink_type = input(f"Which type of drink would you like to search for? (Hit ENTER to quit)\n[1] Hot Drinks \n[2] Soft Drinks \n[3] Alcoholic Drinks \nEnter here: ")
    if drink_type == "":
        sn_nav_options()
    search_entry = str(input(f"\nWhat drink would you like to search for? (Hit ENTER to quit)\nEnter here: ").capitalize())
    if drink_type == "":
        sn_nav_options()
    elif drink_type == "1":
        hot_drinks = perdb.load_tables("hot_drinks")
        for drinks in hot_drinks:
            if search_entry in drinks.drink_choice:
                print(f"{drinks.drink_choice}, {drinks.milk_choice}, {drinks.strength_choice}, {drinks.sugar_choice}")
                # nav_options()
            else:
                continue
        not_found = input("\nDid you find what you were after, would you like to add a new drinks? Y/N \nEnter here: ")
        if not_found == "Y":
            s4_add_drinks()
        else:
            sn_nav_options()
    elif drink_type == "2":
        soft_drinks = perdb.load_tables("soft_drinks")
        for drink in soft_drinks:
            if search_entry in drink.drink_choice:
                print(f"{drink.drink_choice}, {drink.drink_quantity} ml")
            else:
                continue
        not_found = input("\nDid you find what you were after, would you like to add a new drinks? Y/N \nEnter here: ")
        if not_found == "Y":
            s4_add_drinks()
        else:
            sn_nav_options()
    elif drink_type == "3":
        alcoholic_drinks = perdb.load_tables("alcoholic_drinks")
        for drink in alcoholic_drinks:
            if search_entry in drink.drink_choice:
                print(f"{drink.drink_choice}, {drink.drink_quantity} ml")
            else:
                continue
        not_found = input("\nDid you find what you were after, would you like to add a new drinks? Y/N \nEnter here: ")
        if not_found == "Y":
            s4_add_drinks()
        else:
            sn_nav_options()
    else:
        sn_nav_options()


def s3_create_person():
    try:
        while True:
            first_name = input("What it the first name of the the person you would like to add to the app?: (Hit "
                               "ENTER to quit) ")
            if first_name == "":  # Break out from the loop when user hits ENTER
                sn_nav_options()
            surname = input(f"What is {first_name}'s surname? ")
            age = int(input(f"What is {first_name}'s age? "))
            new_person = perdb.Person(first_name, surname, age)
            people.append(new_person)
            perdb.save_people(new_person)
            sn_nav_options()
    except:
        sn_nav_options()


def s4_add_drinks():
    try:
        drink_type = input(f"What type of drink would you like to input:\n[1] Hot Drink\n[2] Soft Drink\n[3] Alcoholic "
                           f"\n(Hit ENTER to quit)  ")
        if drink_type == "":  # Break out from the loop when user hits ENTER
            sn_nav_options()
        elif drink_type == "1":
            print(f"\nBelow is a list of hot drinks in BrIW\n")
            perprint.print_class_dict(hot_drinks)
            drink_choice = str(input("\nWhat hot drink would you like to add?: ").title())
            milk_choice = str(input(f"Is that {drink_choice} white or black?: ").lower())
            strength_choice = str(input(f"What strength should the {drink_choice} be?: ").lower())
            sugar_choice = int(input(f"How many sugars does the {drink_choice} have? (Enter number of teaspoons): "))
            new_hot_drink = perdb.HotDrinks(drink_choice, milk_choice, strength_choice, sugar_choice)
            perdb.save_drinks([new_hot_drink], "Hot")
            hot_drinks.append(new_hot_drink)
        elif drink_type == "2":
            print(f"\nBelow is a list of soft drinks in BrIW\n")
            perprint.print_class_dict(soft_drinks)
            drink_choice = str(input(f"What soft drink would you like to add?: ").title())
            drink_quantity = input(f"What {drink_choice} quantity would you like to save (in ml)?: ")
            new_soft_drink = perdb.SoftDrinks(drink_choice, drink_quantity)
            perdb.save_drinks([new_soft_drink], "Soft")
            soft_drinks.append(new_soft_drink)
        elif drink_type == "3":
            print(f"\nBelow is a list of alcoholic drinks in BrIW\n")
            perprint.print_class_dict(alcoholic_drinks)
            drink_choice = str(input(f"What alcoholic drink would you like to save?: ").title())
            drink_quantity = input(f"What {drink_choice} quantity would you like to save (in ml)?: ")
            new_alcy_drink = perdb.AlcyDrinks(drink_choice, drink_quantity)
            perdb.save_drinks([new_alcy_drink], "Alcy")
            alcoholic_drinks.append(new_alcy_drink)
        else:
            sn_nav_options()
    except:
        sn_nav_options()


def s5_delete_person():
    people_list = perdb.load_tables("people")
    delete_person = str(input("Type the first and last name of the person you would like to delete : ").capitalize().strip())
    split_delete_person = delete_person.split(", ")
    first_name = split_delete_person[0]
    surname = split_delete_person[1].capitalize()
    for person in people_list:
        if delete_person == "":
            break
        elif (first_name, surname) == (person.first_name, person.surname):
            delete_confirmation = input(f"{person.first_name} {person.surname}, {person.age} was located, are you sure "
                                        f"you want to delete them? Enter Y/N \nEnter here: ")
            if delete_confirmation == "Y":
                perdb.delete_person(person)
            else:
                continue
        else:
            break
    sn_nav_options()


def s6_delete_drinks_type():
    drink_type = input(f"What type of drink would you like to delete?\n[1] Hot Drink\n[2] Soft Drink\n[3] Alcoholic "
                       f"Drink (Hit ENTER to quit)  ")
    if drink_type == "1":
        hot_drinks = perdb.load_tables("hot_drinks")
        delete_drink = str(input("What hot drink would you like to delete?").capitalize())
        for hotdrinks in hot_drinks:
            if delete_drink == "":
                break
            elif delete_drink == hotdrinks.drink_choice:
                perdb.delete_drinks("Hot", hotdrinks)
    elif drink_type == "2":
        soft_drinks = perdb.load_tables("soft_drinks")
        delete_drink = str(input("What soft drink would you like to delete?").capitalize())
        for softdrinks in soft_drinks:
            if delete_drink == "":
                break
            elif delete_drink == softdrinks.drink_choice:
                perdb.delete_drinks("Soft", softdrinks)
    elif drink_type == "3":
        delete_drink = str(input("What alcoholic drink would you like to delete?").capitalize())
        for alcydrinks in alcoholic_drinks:
            if delete_drink == "":
                break
            elif delete_drink == alcydrinks.drink_choice:
                perdb.delete_drinks("Alcy", alcydrinks)
        else:
            sn_nav_options()
    sn_nav_options()


def s7_drinks_pref_menu():
    preferences_selection = input("""What type of drinks preference would you like to add? \n[A] Hot Drink \n[B] Soft Drink \n[C] Alcoholic Drink \n Enter Here: """)
    try:
        if preferences_selection == "A":
            os.system("Clear")
            s7a_add_hot_drink_prefs()
        elif preferences_selection == "B":
            os.system("Clear")
            print("These are the current soft drinks preferences stored by the app. To overwrite a preference simply retype their preference as below.")
            print(soft_drinks_pref)
            s7b_add_soft_or_alcy_prefs(soft_drinks_pref)
            print(soft_drinks_pref)
            persave.save_csv_dictionary("persistence/softdrinksprefs.csv", soft_drinks_pref)
        elif preferences_selection == "C":
            os.system("Clear")
            print("These are the current alcoholic drinks preferences stored by the app. To overwrite a preference simply retype their preference as below.")
            print(alcoholic_drinks_pref)
            s7b_add_soft_or_alcy_prefs(alcoholic_drinks_pref)
            print(alcoholic_drinks_pref)
            persave.save_csv_dictionary("persistence/alocoholicdrinksprefs.csv", alcoholic_drinks_pref)
        else:
            os.system("Clear")
            print("Sorry, this is an invalid input")
            sn_nav_options()
    except:
        sn_nav_options()


def s7a_add_hot_drink_prefs():
    while True:
        person = input("Who's hot drink preferences would you like to save to the app'?: (Hit ENTER to quit)\n")
        if person == "":  # Break out from the loop when user hits ENTER
            break
        else:
            hot_drink_choice = input(f"What hot drink would {person} like?: ")
            hot_drink_milk = input(f"To you take that black or white?: ")
            hot_drink_strength = input(f"What strength would you like that?: ")
            hot_drink_sugar = input(f"How many sugars would you like?: ")
            hot_drinks_pref[person] = [hot_drink_choice, hot_drink_milk, hot_drink_strength, hot_drink_sugar]
            persave.save_hot_drinks("persistence/hotdrinksprefs.csv", hot_drinks_pref)
    sn_nav_options()


def s7b_add_soft_or_alcy_prefs(dictionary):
    preference = input("""Add a person and preference in format of "person: drink": """)
    try:
        split_preference = preference.strip().split(": ")
        person = split_preference[0]
        drink = split_preference[1]
        dictionary[person] = drink
        persave.save_csv_dictionary("persistence/alocoholicdrinksprefs.csv", alcoholic_drinks_pref)
        persave.save_csv_dictionary("persistence/softdrinksprefs.csv", soft_drinks_pref)
        return dictionary
    except:
        sn_nav_options()


def s8_print_functions():
    print_choice = str(input(f"| What would you like to print:\n[A] People list\n[B] Drinks list\n[C] Hot Drinks Prefs\n[D] Soft Drinks Prefs\n[E] Alcoholic Drinks Prefs\n[F] Current Round\n Enter Here: ").upper())
    if print_choice == "A":
        os.system("Clear")
        perprint.print_class_dict(people)
    elif print_choice == "B":
        os.system("Clear")
        s8a_print_drinks_lists()
    elif print_choice == "C":
        os.system("Clear")
        print(f" |  Hot Drinks Preferences  |")
        count = 1
        for key, value in hot_drinks_pref.items():
            print(f" | {count}. {key}'s hot drink pref is {value[0]}, {value[1]}, {value[2]} with {value[3]} sugar(s).")
            count += 1
    elif print_choice == "D":
        os.system("Clear")
        print(f" |  Soft Drinks Preferences")
        count = 1
        for key, value in soft_drinks_pref.items():
            print(f" | {count}. {key}'s drink of choice is {value}")
            count += 1
    elif print_choice == "E":
        os.system("Clear")
        print(" |  Alcoholic Drinks Preferences")
        count = 1
        for key, value in alcoholic_drinks_pref.items():
            print(f" | {count}. {key}'s drink of choice is {value}")
            count += 1
    elif print_choice == "F":
        os.system("Clear")
        print(" | Drinks Round |")
        count = 1
        for key, value in new_round.items():
            print(f" | {count}. {key}'s would like a {value}")
            count += 1
    else:
        os.system("Clear")
        print("This is an invalid input")
        sn_nav_options()

def s8a_print_drinks_lists():
    print("""\nThese are the drinks available on the app \nHOT DRINKS: """)
    perprint.print_class_dict(hot_drinks)
    print("\nSOFT DRINKS: ")
    perprint.print_class_dict(soft_drinks)
    print("\nALCOHOLIC DRINKS: ")
    perprint.print_class_dict(alcoholic_drinks)
    sn_nav_options()


def s9_round_type():
    try:
        brewer = input("Who would like to create a round? \nEnter Here: ")
        if currentDT.hour <= 12:
            print(f"The time is currently: {time}, therefore you should have a hot drink.")
            perround.Drinks(brewer).hot_drinks()
            sn_nav_options()
        elif 13 < currentDT.hour < 18:
            print(f"The time is currently: {time}, therefore you should have a soft drink.")
            perround.Drinks(brewer).soft_drinks()
            sn_nav_options()
        else:
            print(f"The time is currently: {time}, therefore you should have an alcoholic drink.")
            perround.Drinks(brewer).alcoholic_drinks()
            sn_nav_options()
    except:
        sn_nav_options()


# def test_add_preference():
#     # Arrange
#     test_preferences = {}
#     test_preference = "Alex: Wine"
#     expected_outcome = {"Alex": "Wine"}
#
#     # Act
#     actual_outcome = s7b_add_soft_or_alcy_prefs(test_preference, test_preferences)
#
#     # Assert
#     assert actual_outcome == expected_outcome, f"""
#     actual outcome = {actual_outcome}
#     expected outcome = {expected_outcome}"""
#     print("Passed the GDPR test")


if __name__ == "__main__":
    perload.load_hot_drinks_prefs("persistence/hotdrinksprefs.csv", hot_drinks_pref)
    perload.load_csv_dictionary("persistence/alocoholicdrinksprefs.csv", alcoholic_drinks_pref)
    perload.load_csv_dictionary("persistence/softdrinksprefs.csv", soft_drinks_pref)
    people = perdb.load_tables("people")
    hot_drinks = perdb.load_tables("hot_drinks")
    soft_drinks = perdb.load_tables("soft_drinks")
    alcoholic_drinks = perdb.load_tables("alcoholic_drinks")


    initial_options()

    SystemExit