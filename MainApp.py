import os
import datetime
from src import persistence as persave, persistence as perload, persistence as perprint, persistence as perround, \
    persistence as perdb

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
    header("Welcome to the BrIW app!")
    result = input("""Please select which option you would like to use:\n[1] Search People List\n[2] Search Drinks List
    \n[3] Add Person\n[4] Add Drink\n[5] Delete Person\n[6] Delete Drinks\n[7] Choose Preferences\n[8] Print Functions 
    \n[9] Take Round\n[10] Exit App \nEnter Here: """)
    initial_function(result)# evokes the if function (menu) within the "Initial_Function"


def initial_function(number): # Defines what outcome is associated with each input from initial options
    if number == "1": # Search person
        s1_search_people()
    elif number == "2": # Search drinks
        s2_search_drinks()
    elif number == "3": # Create Person
        s3_create_person()
    elif number == "4": # Create Drink
        s4_add_drinks()
    elif number == "5": # Delete Person
        s5_delete_person()
    elif number == "6": # Delete Drinks
        s6_delete_drinks_type()
    elif number == "7": # Choose Drinks Prefs
        s7_drinks_pref_menu()
    elif number == "8": # Print stored info
        s8_print_functions()
    elif number == "9": # Round Builder
        s9_round_type()
    elif number == "10": # Exit App
        os.system("Clear")
        print("Catch you later")
        SystemExit()

    else:
        print("This is an invalid input, what would you like to do?")
        initial_options()


def sn_nav_options(): # Once operation is complete what will the user want to do next? (if function)
    print_line()
    numbertwo = input("""Please select your next option:\n[1] Return to main menu\n[2] Exit the app\nEnter Here: """)
    if numbertwo == "1":
        initial_options()
    elif numbertwo == "2":
        os.system("Clear")
        print("Catch you later")
        SystemExit()


def s1_search_people():
    people = perdb.load_tables("people")
    header("    Search People")
    search_entry = str(input(f"Enter first name, surname or age (Hit ENTER to quit) \nEnter here: ").capitalize())
    try:
        for person in people:
            if search_entry == "":
                break
            elif search_entry in (person.first_name, person.surname, person.age):
                print(f"{person.first_name} {person.surname}, {person.age}")
            else:
                continue
    except:
        print("Sorry")
        not_found = input(f"\nWould you like to add someone? Y/N (Hit ENTER to quit) \nEnter here: ")
        if not_found == "Y":
            s3_create_person()
        else:
            sn_nav_options()


def s2_search_drinks():
    header("    Search Drinks")
    drink_type = input(f"Which type of drink are you looking for? (Hit ENTER to quit)\n[1] Hot Drinks \n[2] "
                       f"Soft Drinks \n[3] Alcoholic Drinks \nEnter here: ")
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
            else:
                continue
        not_found = input("\nWould you like to add a new drink? Y/N (Hit ENTER to quit) \nEnter here: ")
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
    header("    Add Drinker")
    try:
        while True:
            first_name = input("What is the new drinkers first name?: (Hit ENTER to quit) \nEnter here:")
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
    header("    Add Drinks")
    try:
        drink_type = input(f"What type of drink would you like to input:\n[1] Hot Drink\n[2] Soft Drink\n[3] Alcoholic "
                           f"\n(Hit ENTER to quit)  ")
        if drink_type == "":  # Break out from the loop when user hits ENTER
            sn_nav_options()
        elif drink_type == "1":
            header(f"Hot drinks in BrIW")
            perprint.print_hot_drinks(perdb.load_tables("hot_drinks"))
            print_line()
            drink_choice = str(input("\nWhat hot drink would you like to add?: ").title())
            if drink_choice == "":
                sn_nav_options()
            else:
                milk_choice = str(input(f"Is that {drink_choice} white or black?: ").lower())
                strength_choice = str(input(f"What strength should the {drink_choice} be?: ").lower())
                sugar_choice = int(input(f"How many sugars does the {drink_choice} have? (Enter number of teaspoons): "))
                new_hot_drink = perdb.HotDrinks(drink_choice, milk_choice, strength_choice, sugar_choice)
                perdb.save_drinks([new_hot_drink], "Hot")
                hot_drinks.append(new_hot_drink)
        elif drink_type == "2":
            header(f"Soft drinks in BrIW")
            perprint.print_soft_or_alcy_drinks(perdb.load_tables("soft_drinks"))
            print_line()
            drink_choice = str(input(f"\nWhat soft drink would you like to add?: ").title())
            if drink_choice == "":
                sn_nav_options()
            else:
                drink_quantity = input(f"What {drink_choice} quantity would you like to save (in ml)?: ")
                new_soft_drink = perdb.SoftDrinks(drink_choice, drink_quantity)
                perdb.save_drinks([new_soft_drink], "Soft")
                soft_drinks.append(new_soft_drink)
        elif drink_type == "3":
            header(f"Alcoholic drinks in BrIW")
            perprint.print_soft_or_alcy_drinks(perdb.load_tables("alcoholic_drinks"))
            print_line()
            drink_choice = str(input(f"\nWhat alcoholic drink would you like to save?: ").title())
            if drink_choice == "":
                sn_nav_options()
            else:
                drink_quantity = input(f"What {drink_choice} quantity would you like to save (in ml)?: ")
                new_alcy_drink = perdb.AlcyDrinks(drink_choice, drink_quantity)
                perdb.save_drinks([new_alcy_drink], "Alcy")
                alcoholic_drinks.append(new_alcy_drink)
        else:
            sn_nav_options()
    except:
        sn_nav_options()


def s5_delete_person():
    header("    Search People")
    people_list = perdb.load_tables("people")
    delete_person = str(input("Type the first and last name of the who you want to delete\nEnter here: ").capitalize().strip())
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
    header("    Delete Drinks")
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
    header("   Drinks Preferences")
    preferences_selection = input("""What type of drinks preference would you like to add? \n[A] Hot Drink \n
    [B] Soft Drink \n[C] Alcoholic Drink \nEnter Here: """)
    try:
        if preferences_selection == "A":
            header("Stored Alcoholic Drinks")
            print("To overwrite a preference simply retype their preference as below.")
            perprint.print_hot_dicts(hot_drinks_pref)
            s7a_add_hot_drink_prefs()
        elif preferences_selection == "B":
            os.system("Clear")
            header(" Stored Soft Drinks")
            print("To overwrite a preference simply retype their preference as below.")
            perprint.print_soft_or_alcy_dicts(soft_drinks_pref)
            s7b_add_soft_or_alcy_prefs(soft_drinks_pref)
            persave.save_csv_dictionary("src/persistence/softdrinksprefs.csv", soft_drinks_pref)
            sn_nav_options()
        elif preferences_selection == "C":
            header("Stored Alcoholic Drinks")
            print("To overwrite a preference simply retype their preference as below.")
            perprint.print_soft_or_alcy_dicts(alcoholic_drinks_pref)
            s7b_add_soft_or_alcy_prefs(alcoholic_drinks_pref)
            persave.save_csv_dictionary("src/persistence/alcoholicdrinksprefs.csv", alcoholic_drinks_pref)
            sn_nav_options()
        else:
            os.system("Clear")
            print("Sorry, this is an invalid input")
            sn_nav_options()
    except:
        sn_nav_options()


def s7a_add_hot_drink_prefs():
    while True:
        person = input("\nWho's hot drink preferences would you like to save to the app'?: \n(Hit ENTER to exit) Enter here: ")
        if person == "":  # Break out from the loop when user hits ENTER
            break
        else:
            hot_drink_choice = input(f"What hot drink would {person} like?: ")
            hot_drink_milk = input(f"To you take that black or white?: ")
            hot_drink_strength = input(f"What strength would you like that?: ")
            hot_drink_sugar = input(f"How many sugars would you like?: ")
            hot_drinks_pref[person] = [hot_drink_choice, hot_drink_milk, hot_drink_strength, hot_drink_sugar]
            persave.save_hot_drinks("src/persistence/hotdrinksprefs.csv", hot_drinks_pref)
            return hot_drinks_pref
    sn_nav_options()


def s7b_add_soft_or_alcy_prefs(dictionary):
    while True:
        preference = input(f"\nAdd a person and preference in format of 'person: drink'\n(Hit ENTER to exit) Enter here: ")
        if preference == "":  # Break out from the loop when user hits ENTER
            break
        else:
            split_preference = preference.strip().split(": ")
            person = split_preference[0]
            drink = split_preference[1]
            dictionary[person] = drink
        return dictionary

def s8_print_functions():
    header("   Print Functions")
    print_choice = str(input(f"| What would you like to print:\n[A] People list\n[B] Drinks list\n[C] Hot Drinks Prefs"
                             f"\n[D] Soft Drinks Prefs\n[E] Alcoholic Drinks Prefs\n[F] Current Round\nEnter Here: ").
                       upper())
    if print_choice == "A":
        os.system("Clear")
        perprint.print_person(people)
        sn_nav_options()
    elif print_choice == "B":
        os.system("Clear")
        s8a_print_drinks_lists()
        sn_nav_options()
    elif print_choice == "C":
        header("Hot Drinks Preferences")
        perprint.print_hot_dicts(hot_drinks_pref)
        sn_nav_options()
    elif print_choice == "D":
        header("Soft Drinks Preferences")
        perprint.print_soft_or_alcy_dicts(soft_drinks_pref)
        sn_nav_options()
    elif print_choice == "E":
        header("Alcoholic Drinks Preferences")
        perprint.print_soft_or_alcy_dicts(alcoholic_drinks_pref)
        sn_nav_options()
    elif print_choice == "F":
        os.system("Clear")
        header(" Drinks Round")
        count = 1
        for key, value in new_round.items():
            print(f" | {count}. {key}'s would like a {value}")
            count += 1
        sn_nav_options()
    else:
        os.system("Clear")
        print("This is an invalid input")
        sn_nav_options()


def s8a_print_drinks_lists():
    header("    Saved Drinks")
    print("                       Hot Drinks")
    print_line()
    perprint.print_hot_drinks(perdb.load_tables("hot_drinks"))
    print_line()
    print("                       Soft Drinks")
    print_line()
    perprint.print_soft_or_alcy_drinks(perdb.load_tables("soft_drinks"))
    print_line()
    print("                      Alcoholic Drinks")
    print_line()
    perprint.print_soft_or_alcy_drinks(perdb.load_tables("alcoholic_drinks"))
    sn_nav_options()


def s9_round_type():
    header("  Round Builder 1.0")
    try:
        brewer = input("Who would like to create a round? \nEnter Here: ")
        if currentDT.hour <= 15:
            print(f"It is currently {time}, therefore you should have a hot drink.")
            perround.Drinks(brewer).hot_drinks()
            sn_nav_options()
        elif 16 < currentDT.hour < 18:
            print(f"It is currently {time}, therefore you should have a soft drink.")
            perround.Drinks(brewer).soft_drinks()
            sn_nav_options()
        else:
            print(f"It is currently: {time}, therefore you should have an alcoholic drink.")
            perround.Drinks(brewer).alcoholic_drinks()
            sn_nav_options()
    except:
        sn_nav_options()


def print_line():
    print("+-------------------------------------------------------------+")


def header(header_text):
    os.system("Clear")
    print("+-------------------------------------------------------------+")
    print(f"                   {header_text}                              ")
    print("+-------------------------------------------------------------+")


if __name__ == "__main__":
    perload.load_hot_drinks_prefs("src/persistence/hotdrinksprefs.csv", hot_drinks_pref)
    perload.load_csv_dictionary("src/persistence/alcoholicdrinksprefs.csv", alcoholic_drinks_pref)
    perload.load_csv_dictionary("src/persistence/softdrinksprefs.csv", soft_drinks_pref)
    people = perdb.load_tables("people")
    hot_drinks = perdb.load_tables("hot_drinks")
    soft_drinks = perdb.load_tables("soft_drinks")
    alcoholic_drinks = perdb.load_tables("alcoholic_drinks")


    initial_options()

    SystemExit