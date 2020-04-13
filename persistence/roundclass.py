import csv

hot_drinks_prefs = {"Sam":["Coffee","black","mild","None"],"Lewis":["Americano","black","strong","none"]}
soft_drinks_pref = {"Sam":["Fanta"],"Lewis":["San Pel"]}
alcoholic_drinks_pref = {"Sam":["Lager"],"Lewis":["Bitter"]}

class NewRound:
    def __init__(self, brewer_name):
        self.brewer = brewer_name
        self.hot_round = {}
        self.soft_round = {}
        self.alcohol_round = {}

    def hot_drinks(self):
        try:
            brewer_hot_drink = hot_drinks_prefs[self.brewer]
            print(f"Hi {self.brewer} your stored hot drink preference is {brewer_hot_drink[0]}, {brewer_hot_drink[1]} and {brewer_hot_drink[2]} with {brewer_hot_drink[3]} sugar(s).")
            brewer_choice = input("""Are you having the usual? \nEnter Y / N: """)
            if brewer_choice == "Y":
                self.hot_round[self.brewer] = (brewer_hot_drink[0], brewer_hot_drink[1], brewer_hot_drink[2], brewer_hot_drink[3])
                print(self.hot_round)
            else:
                print("What can I get you?")
                hot_drink_choice = input(f"What hot drink would you like?: ")
                hot_drink_milk = input(f"To you take that black or white?: ")
                hot_drink_strength = input(f"What strength would you like that?: ")
                hot_drink_sugar = input(f"How many sugars would you like?: ")
                self.hot_round[self.brewer] = (hot_drink_choice, hot_drink_milk, hot_drink_strength, hot_drink_sugar)
        except:
            print(f"Sorry {self.brewer}, unfortunately I don't have your hot drinks preferences stored.")
            hot_drink_choice = input(f"What hot drink would you like?: ")
            hot_drink_milk = input(f"To you take that black or white?: ")
            hot_drink_strength = input(f"What strength would you like that?: ")
            hot_drink_sugar = input(f"How many sugars would you like?: ")
            self.hot_round[self.brewer] = (hot_drink_choice, hot_drink_milk, hot_drink_strength, hot_drink_sugar)
            # Add save to preferences file
        while True:
            drinker = input("Who else would you like to include in this round?: (Hit ENTER to quit)\n")
            if drinker == "":  # Break out from the loop when user hits ENTER
                break
            hot_drink_choice = input(f"What hot drink would you like?: ")
            hot_drink_milk = input(f"To you take that black or white?: ")
            hot_drink_strength = input(f"What strength would you like that?: ")
            hot_drink_sugar = input(f"How many sugars would you like?: ")
            self.hot_round[drinker] = (hot_drink_choice, hot_drink_milk, hot_drink_strength, hot_drink_sugar)
        print(self.hot_round)

    def soft_drinks(self):
        try:
            brewer_soft_drink = soft_drinks_pref[self.brewer]
            print(f"Hi {self.brewer} your stored soft drink preference is {brewer_soft_drink[0]}")
            brewer_choice = input("""Are you having the usual? \nEnter Y / N: """)
            if brewer_choice == "Y":
                self.soft_round[self.brewer] = brewer_soft_drink[0]
                print(self.soft_round)
            else:
                soft_drink_choice = input(f"What soft drink would you like?: ")
                self.soft_round[self.brewer] = (soft_drink_choice)
                print(self.soft_round)
        except:
            print(f"Sorry {self.brewer}, unfortunately I don't have your soft drinks preference stored.")
            soft_drink_choice = input(f"What soft drink would you like {self.brewer}?: ")
            self.soft_round[self.brewer] = (soft_drink_choice)
            print(self.soft_round)
            # Add save to preferences file
        while True:
            drinker = input("Who else would you like to include in this round?: (Hit ENTER to quit)\n")
            if drinker == "":  # Break out from the loop when user hits ENTER
                break
            soft_drink_choice = input(f"What soft drink would they like?: ")
            self.soft_round[drinker] = (soft_drink_choice)
        print(self.soft_round)

    def alcoholic_drinks(self):
        try:
            brewer_alcoholic = alcoholic_drinks_pref[self.brewer]
            print(f"Hi {self.brewer} your stored alcoholic drink preference is {brewer_alcoholic[0]}")
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
            alcoholic_drink_choice = input(f"What boozy drink would {self.brewer} like?: ")
            self.alcohol_round[self.brewer] = (alcoholic_drink_choice)
            print(self.alcohol_round)
            # Add save to preferences file
        while True:
            drinker = input("Who else would you like to include in this round?: (Hit ENTER to quit)\n")
            if drinker == "":  # Break out from the loop when user hits ENTER
                break
            alcoholic_drink_choice = input(f"What boozy drink would {drinker} like?: ")
            self.alcohol_round[drinker] = (alcoholic_drink_choice)
        print(self.alcohol_round)


my_round = NewRound("Sam")
my_round.alcoholic_drinks()


