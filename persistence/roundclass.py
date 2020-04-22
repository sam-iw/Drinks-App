import persistence.load as perload
import persistence.save as persave


hot_drinks_pref = {}
soft_drinks_pref = {}
alcoholic_drinks_pref = {}

# perload.load_hot_drinks_prefs("persistence/hotdrinksprefs.csv", hot_drinks_pref)
# perload.load_csv_dictionary("persistence/alocoholicdrinksprefs.csv", alcoholic_drinks_pref)
# perload.load_csv_dictionary("persistence/softdrinksprefs.csv", soft_drinks_pref)

class NewRound:
    def __init__(self, brewer_name):
        self.brewer = brewer_name
        self.hot_round = {}
        self.soft_round = {}
        self.alcohol_round = {}

    def hot_drink_input(self, who):
        hot_drink_choice = input(f"What hot drink would {who} like?: ")
        hot_drink_milk = input(f"To you take that black or white?: ")
        hot_drink_strength = input(f"What strength would you like that?: ")
        hot_drink_sugar = input(f"How many sugars would you like?: ")
        self.hot_round[who] = [hot_drink_choice, hot_drink_milk, hot_drink_strength, hot_drink_sugar]
        hot_drinks_pref[who] = (hot_drink_choice, hot_drink_milk, hot_drink_strength, hot_drink_sugar)
        persave.save_hot_drinks("persistence/hotdrinksprefs.csv", hot_drinks_pref)


class Drinks:
    def hot_drinks(self):
        try:
            brewer_hot_drink = hot_drinks_pref[self.brewer]
            print(f"Hi {self.brewer}, your stored hot drink preference is {brewer_hot_drink[0]}, {brewer_hot_drink[1]} and {brewer_hot_drink[2]} with {brewer_hot_drink[3]} sugar(s).")
            brewer_choice = input("""Are you having the usual? \nEnter Y / N: """)
            if brewer_choice == "Y":
                self.hot_round[self.brewer] = (brewer_hot_drink[0], brewer_hot_drink[1], brewer_hot_drink[2], brewer_hot_drink[3])
                print(self.hot_round)
            else:
                print("What can I get you?")
                self.hot_drink_input(self.brewer)
        except:
            print(f"Sorry {self.brewer}, unfortunately I don't have your hot drinks preferences stored.")
            self.hot_drink_input(self.brewer)

        while True:
            drinker = input("Who else would you like to include in this round?: (Hit ENTER to quit)\n")
            if drinker == "":  # Break out from the loop when user hits ENTER
                break
            self.hot_drink_input(drinker)
        print(self.hot_round)

    def soft_drinks(self):
        try:
            brewer_soft_drink = soft_drinks_pref[self.brewer]
            print(f"Hi {self.brewer}, your stored soft drink preference is {brewer_soft_drink}.")
            brewer_choice = input("""Are you having the usual? \nEnter Y / N: """)
            if brewer_choice == "Y":
                self.soft_round[self.brewer] = (brewer_soft_drink)
                print(self.soft_round)
            else:
                soft_drink_choice = input(f"What soft drink would you like?: ")
                self.soft_round[self.brewer] = (soft_drink_choice)
                print(self.soft_round)
        except:
            print(f"Sorry {self.brewer}, unfortunately I don't have your soft drinks preference stored.")
            soft_drink_choice = input(f"What soft drink would you like {self.brewer}?: ")
            self.soft_round[self.brewer] = (soft_drink_choice)
            soft_drinks_pref[self.brewer] = (soft_drink_choice)
            print(self.soft_round)
            persave.save_csv_dictionary("persistence/softdrinksprefs.csv", soft_drinks_pref)
        while True:
            drinker = input("Who else would you like to include in this round?: (Hit ENTER to quit)\n")
            if drinker == "":  # Break out from the loop when user hits ENTER
                break
            soft_drink_choice = input(f"What soft drink would {drinker} like?: ")
            self.soft_round[drinker] = (soft_drink_choice)
            soft_drinks_pref[drinker] = (soft_drink_choice)
            persave.save_csv_dictionary("persistence/soft_drinks_pref.csv", soft_drinks_pref)
        print(self.soft_round)

    def alcoholic_drinks(self):
        try:
            brewer_alcoholic = alcoholic_drinks_pref[self.brewer]
            print(f"Hi {self.brewer}, your stored alcoholic drink preference is {brewer_alcoholic[0]}.")
            brewer_choice = input("""Are you having the usual? \nEnter Y / N: """)
            if brewer_choice == "Y":
                self.alcohol_round[self.brewer] = brewer_alcoholic[0]
                print(self.alcohol_round)
            else:
                alcoholic_drink_choice = input(f"What boozy drink would {self.brewer} like?: ")
                self.alcohol_round[self.brewer] = (alcoholic_drink_choice)
                print(self.alcohol_round)
        except:
            print(f"Sorry {self.brewer}, unfortunately I don't have your boozy drinks preference stored.")
            alcoholic_drink_choice = input(f"WhatALTER TABLE people ADD drinker_surname VARCHAR(100) AFTER drinker_name; boozy drink would {self.brewer} like?: ")
            self.alcohol_round[self.brewer] = (alcoholic_drink_choice)
            alcoholic_drinks_pref[self.brewer] = (alcoholic_drink_choice)
            print(self.alcohol_round)
            persave.save_csv_dictionary("persistence/alocoholicdrinksprefs.csv", alcoholic_drinks_pref)
        while True:
            drinker = input("Who else would you like to include in this round?: (Hit ENTER to quit)\n")
            if drinker == "":  # Break out from the loop when user hits ENTER
                break
            alcoholic_drink_choice = input(f"What boozy drink would {drinker} like?: ")
            self.alcohol_round[drinker] = (alcoholic_drink_choice)
            soft_drinks_pref[drinker] = (alcoholic_drink_choice)
            persave.save_csv_dictionary("persistence/alcoholic_drinks_pref.csv", alcoholic_drinks_pref)
        print(self.alcohol_round)


# class Person:
#     def __init__(self, first_name, surname, age, id=None):
#         self.first_name = first_name
#         self.surname = surname
#         self.age = age
#         self.id = id
#
#     def print(self):
#         print(f"{self.first_name}, {self.surname}, {self.age}")



# my_round = NewRound("Sam")
# my_round.hot_drinks()