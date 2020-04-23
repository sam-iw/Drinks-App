from os import environ
import pymysql


def get_connection(): # function to get the connection string using: pymysql.connect(host, username, password, database)
    db_connection = pymysql.connect(
        environ.get('DB_HOST'), #host
        environ.get('DB_USER'), #username
        environ.get('DB_PW'), #password
        environ.get('DB_NAME') #database
        )
    print("Connection with DB established, get in")
    return db_connection


class Person:
    def __init__(self, first_name, surname, age, id=None):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.id = id

    def print(self):
        print(f"{self.first_name} {self.surname}, is {self.age} years old.")


class HotDrinks:
    def __init__(self, drink_choice, milk_choice, strength_choice, sugar_choice, id=None):
        self.drink_choice = drink_choice
        self.milk_choice = milk_choice
        self.strength_choice = strength_choice
        self.sugar_choice = sugar_choice
        self.id = id

    def print(self):
        print(f"{self.drink_choice}, with {self.milk_choice} milk(s), {self.strength_choice} with {self.sugar_choice} "
              f"sugar(s).")


class SoftDrinks:
    def __init__(self, drink_choice, drink_quantity, id=None):
        self.drink_choice = drink_choice
        self.drink_quantity = drink_quantity
        self.id = id

    def print(self):
        print(f"{self.drink_choice}, {self.drink_quantity} ml")


class AlcyDrinks:
    def __init__(self, drink_choice, drink_quantity, id=None):
        self.drink_choice = drink_choice
        self.drink_quantity = drink_quantity
        self.id = id

    def print(self):
        print(f"{self.drink_choice}, {self.drink_quantity} ml")


def load_tables(tables):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {tables}")
    table_list = []
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        elif tables == "people":
            person = Person(row[1], row[2], row[3], row[0])  # row 0 last because it's a default
            table_list.append(person)
        elif tables == "hot_drinks":
            hot_drinks = HotDrinks(row[1], row[2], row[3], row[4], row[0])  # row 0 last because it's a default
            table_list.append(hot_drinks)
        elif tables == "soft_drinks":
            soft_drinks = SoftDrinks(row[1], row[2], row[0])  # row 0 last because it's a default
            table_list.append(soft_drinks)
        elif tables == "alcoholic_drinks":
            alcoholic_drinks = AlcyDrinks(row[1], row[2], row[0])  # row 0 last because it's a default
            table_list.append(alcoholic_drinks)
        else:
            return
    cursor.close()
    connection.close()
    return table_list


def save_people(people):
    connection = get_connection()
    cursor = connection.cursor()
    for person in people:
        if person.id == None:
            args = (person.first_name, person.surname, person.age)
            cursor.execute("INSERT INTO people (drinker_first_name, drinker_surname, drinker_age) VALUES (%s, %s, %s)",
                           args)
    connection.commit()
    cursor.close()
    connection.close()


def save_drinks(list, drink_type):
    connection = get_connection()
    cursor = connection.cursor()
    for drink in list:
        if drink_type == "Hot":
            args = (drink.drink_choice, drink.milk_choice, drink.strength_choice, drink.sugar_choice)
            cursor.execute("INSERT INTO hot_drinks (hot_drink, milk, drink_strength, sugar) VALUES (%s, %s, %s, %s)", args)
        elif drink_type == "Soft":
            args = (drink.drink_choice, drink.drink_quantity)
            cursor.execute("INSERT INTO soft_drinks (soft_drink, soft_quantity_ml) VALUES (%s, %s)", args)
        elif drink_type == "Alcy":
            args = (drink.drink_choice, drink.drink_quantity)
            cursor.execute("INSERT INTO alcoholic_drinks (alcy_drink, alcy_quantity_ml) VALUES (%s, %s)", args)
        else:
            break
    connection.commit()
    cursor.close()
    connection.close()



