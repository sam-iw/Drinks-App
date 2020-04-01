import os
import time

os.system("Clear")

people = []
drinks = []
preferences = {}
new_round = {}

class Round:
    # constructor with brewer as an argument
    def __init__(self, brewer):
        # assign a brewer
        self.brewer = brewer
        # set active to true
        self.active = True
        # create an empty dictionary
        self.orders = {brewer: preferences[brewer]}

    # add person method
    def add_person(self, name):
        # only add if round is active
        if self.active:
            self.orders[name] = preferences[name]
        else:
            print("Sorry this round is closed")

    # set round to inactive method
    def stop_orders(self):
        self.active = False

# Asks for user input which equals result, returns a string
def initial_options():
    os.system("Clear") #Remove / Refresh screen
    result = input("""Please select option you would like to use:\n[1] People List\n[2] Drinks List\n[3] Add Person\n[4] Add Drink\n[5] Delete People\n[6] Delete Drinks\n[7] Choose Preferences\n[8] Print Function (menu)\n[9] Take Round\n[10] Exit\nEnter Here: """)
    Initial_Function(result) #evokes the if function (menu) within the "Initial_Function"

# Defines what outcome is associated with each input from intital options
def Initial_Function(number):
    if number == "1":
        os.system("Clear")
        print("""These are the people on the app: """)
        print_list(people)
        nav_options()   
    elif number == "2":
        os.system("Clear")
        print("""These are the drinks available on the app: """)
        print_list(drinks)
        nav_options()
    elif number == "3":
        os.system("Clear")
        type_entry(people)
        print_list(people)
        save_list("../persistence/people.txt", people)
    elif number == "4":
        os.system("Clear")
        type_entry(drinks)
        save_list("../persistence/drinks.txt", drinks)
        print_list(drinks)
    elif number == "5":
        os.system("Clear")
        delete_inputs(people)
        print_list(people)
    elif number == "6":
        os.system("Clear")
        delete_inputs(drinks)
        print_list(drinks)
    elif number == "7":
        os.system("Clear")
        print(" |  Below Is Everyone's Drink Preferences  |")
        load_dictionary("../preferences.txt", preferences)
        preference = input("""Add a person and preference in format of "person: drink": """)
        add_preference(preference, preferences)
        count = 1
        for key, value in preferences.items():
            print(f" |  {count}. {key}'s drink of choice is {value}  |")
            count += 1
        save_dictionary("../preferences.txt", preferences)
        nav_options()
    elif number == "8":
        os.system("clear")
        print_options()
        nav_options()
    elif number == "9":
        os.system("clear")
        brewer = input("Who would like to create a round? \nEnter Here: ")
        new_round = Round(brewer)
        while True:
            drinker = input("""Add a drinker's name or hit enter to stop adding people: """)
            try:
                if drinker == "":
                    break
                new_round.add_person(drinker)
            except:
                print("""I don't recognise that person, please enter their name and preference below: """)
                add_preference()
                new_round.add_person(drinker)
        print(new_round.orders)
        save_dictionary("../persistence/newround.txt", new_round.orders)
        nav_options()
    elif number == "10":
        os.system("Clear")
        print("Catch you later")
        save_list("../persistence/people.txt", people)
        save_list("../persistence/drinks.txt", drinks)
        exit()
    else:
        print("This is an invalid input")
        initial_options()

# # Create round function
# def create_round():
#     brewer = input("Who would like to create a round? \nEnter Here: ")
#     new_round = Round(brewer)
#     print(f"The brewer for this round is {brewer}")
#     #Is the round active
#     return new_round

# Add person to round, if round is active
# def add_person(current_round):
#     drinker = input("Who would you like to include on this round? \nEnter Here: ")
#     drinker = Round(drinker)
#     current_round.add_person(drinker)
#     Round.orders[drinker] = preferences[drinker]

# Print list function
def print_list(list):
    count = 1
    for items in list:
        print(f" {count} {items}")
        count += 1

# Once operation is complete what will the user want to do next? (if function)
def nav_options():
    numbertwo = input("""Please select your next option:\n[1] Return to main menu\n[2] Exit the options\nEnter Here: """)
    if numbertwo == "1":
        save_list("../persistence/people.txt", people)
        save_list("../persistence/drinks.txt", drinks)
        initial_options()
    elif numbertwo == "2":
        os.system("Clear")
        print("Catch you later")
        save_list("../persistence/people.txt", people)
        save_list("../persistence/drinks.txt", drinks)
        exit()
    else:
        os.system("Clear")
        print("This is an invalid input, please re-select an option.")
        nav_options()

# Print something and evoke navigation menu
def nav_options_with_print(thing):
    print(thing)
    nav_options()

# Generic add entry to list function.
def type_entry(List):
    os.system("Clear")
    print("""The list below is what is currently stored in the app.""")
    print_list(List)
    Entries = input("Enter New Entry: ")
    for Entry in Entries.split(", "):
        List += [Entry]
        print_list(List)
        nav_options()

# Generic delete function that includes an exception rule.
def delete_inputs(List):
    os.system("Clear")
    print("""Below is a list of items currently stored in the app, which would you like to delete?""")
    print_list(List)
    Deletions = input ("Enter what to delete: ")
    try:
        for Deletion in Deletions.split(", "):
            List.remove(Deletion)
        print("""The remaining items stored in the app are below:""")
        print_list(List)
        nav_options()
    except:
        print("""You have made an invalid entry.""")
        nav_options()

def load_dictionary(filepath, dictionary):
    try:
        with open(filepath, "r") as dictionary_file:
            dictionary_lines = dictionary_file.readlines()
            for line in dictionary_lines:
                key_value_pair = line.split(': ')
                key = key_value_pair[0]
                value = key_value_pair[1].strip("\n")
                dictionary[key] = value
    except Exception as error:
        print("oh no, an error occured, please select next option: ")
        print(error)
        nav_options()
    count = 1
    for key, value in dictionary.items():
        print(f" |  {count}. {key}'s drink of choice is {value}")
        count += 1


# Add drinks choices to preference dictionary
def load_preferences():
    print("Currently the drinks preferences below are saved within the app:")
    personal_preferences = open("../preferences.txt", "r")
    read_preferences = personal_preferences.readlines()
    for line in read_preferences:
        key_value_pair = line.split(': ')
        person = key_value_pair[0]
        drink_choice = key_value_pair[1]
        drink_choice = drink_choice.strip("\n")
        preferences[person] = drink_choice
    count = 1
    for key, value in preferences.items():
        print(f" |  {count}. {key}'s drink of choice is {value}  |")
        count += 1

def add_preference(preference, dictionary):
    split_preference = preference.strip().split(": ")
    person = split_preference[0]
    drink = split_preference[1]
    dictionary[person] = drink
    return dictionary

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
    

def save_dictionary(filepath, dictionary):
    try:
        with open(filepath, "w") as dictionary_file:
            for key, value in dictionary.items():# key and values in dict two, dict_two.items()
                dictionary_file.write(f"{key}: {value}" + "\n") # add to the text file, saves it (I think)
    except:
        print("An error occurred (sorry)")
        nav_options()

# def save_preferences():
#     try:
#         personal_preferences = open("preferences.txt", "w") #writing to the dictionary that has previously been opened
#         for person, drink in preferences.items():# key and values in dict two, dict_two.items()
#             personal_preferences.write(f"{person}: {drink}" + '\n') # add to the text file, saves it (I think)
#     except:
#         print("An error occurred, please select what you would like to do next.")
#         nav_options()

# Which person should a drinks preference be assigned?
def choose_person():
    print_list(people)
    Person_Choice = input("Choose which person: ")
    print(f"You selected:  {Person_Choice}")
    return Person_Choice

# Which drink should be assigned to each of the
def choose_drink():
    print_list(drinks)
    Drinks_Choice = input("Choose which drink preference (only one drink per person): ")
    print(f"You selected: {Drinks_Choice}")
    return Drinks_Choice

#
def items_in_list(list):
    count = 1
    for item in list:
        print(f" | {count}. {item} |")
        count += 1

def load_lists(filename, lst):
    try:
        with open(filename, 'r') as file:
            for item in file.readlines():
                item = item.strip()
                lst.append(item)
    except Exception as err:
        print('Something went wrong ' + str(err))

def save_list(filename, lst):
    try:
        with open(filename, 'w') as file:
            for item in lst:
                file.write(item + '\n')
    except Exception as err:
        print('Something went wrong ' + str(err))


load_lists("../persistence/people.txt", people)
load_lists("../persistence/drinks.txt", drinks)
test_add_preference()
time.sleep(2)
initial_options()
load_dictionary("../preferences.txt", preferences)
load_dictionary("../persistence/newround.txt", new_round)

def print_options():
    Print_Choice = input("""What would you like to print:\n[A] Print People\n[B] Print Drinks\n[C] Print Preferences\n[D] Print Round\n Enter Here: """)
    if Print_Choice == "A":
        os.system("Clear")
        print_list(people)
        # generate_table("People", People)
    elif Print_Choice == "B":
        os.system("Clear")
        print_list(drinks)
        # generate_table("Drinks", Drinks)
    elif Print_Choice == "C":
        os.system("Clear")
        print(" |  Preferences  |")
        count = 1
        for key, value in preferences.items():
            print(f" |  {count}. {key}'s drink of choice is {value}  |")
            count += 1
    elif Print_Choice == "D":
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
    items_in_list(list)
    outline()

def items_in_list(list):
    count = 1
    for item in list:
        print(f" | {count}. {item} |")
        count += 1


SystemExit