from os import environ
import pymysql

db_people_list = []
db_drinks_list = []
people = []


def get_connection():# function to get the connection string using: pymysql.connect(host, username, password, database)
    db_connection = pymysql.connect(
        environ.get('DB_HOST'), #host
        environ.get('DB_USER'), #username
        environ.get('DB_PW'), #password
        environ.get('DB_NAME') #database
        )
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
        print(f"{self.drink_choice}, {self.milk_choice.lower()}, {self.strength_choice.lower()} with {self.sugar_choice} "
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


def save_people(person):
    if person.id == None:
        args = (person.first_name, person.surname, person.age)
        sql_query = "INSERT INTO people (drinker_first_name, drinker_surname, drinker_age) VALUES (%s, %s, %s)"
        save_sql(sql_query, args)
        print(f"{person.first_name} {person.surname}, {person.age} was saved to BrIW")


def save_sql(sql_query, args):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(sql_query, args)
    connection.commit()
    cursor.close()
    connection.close()


def save_drinks(list, drink_type):
    for drink in list:
        if drink_type == "Hot":
            args = (drink.drink_choice, drink.milk_choice, drink.strength_choice, drink.sugar_choice)
            sql_query = "INSERT INTO hot_drinks (hot_drink, milk, drink_strength, sugar) VALUES (%s, %s, %s, %s)"
            save_sql(sql_query, args)
            print(f"{drink.drink_choice}, with {drink.milk_choice} milk, {drink.strength_choice} with "
                  f"{drink.sugar_choice} sugar(s) has been saved to BrIW.")
        elif drink_type == "Soft":
            args = (drink.drink_choice, drink.drink_quantity)
            sql_query = "INSERT INTO soft_drinks (soft_drink, soft_quantity_ml) VALUES (%s, %s)"
            save_sql(sql_query, args)
            print(f"{drink.drink_choice}, {drink.drink_quantity}ml has been saved to BrIW.")
        elif drink_type == "Alcy":
            args = (drink.drink_choice, drink.drink_quantity)
            sql_query = "INSERT INTO alcoholic_drinks (alcy_drink, alcy_quantity_ml) VALUES (%s, %s)"
            save_sql(sql_query, args)
            print(f"{drink.drink_choice}, {drink.drink_quantity}ml has been saved to BrIW.")
        else:
            break


def delete_person(person):
    args = person.id
    sql_query = "DELETE FROM people WHERE id=%s"  # %s prevents SQL injection!
    save_sql(sql_query, args)
    print(f"{person.first_name} {person.surname} was deleted")



def delete_drinks(drinks_type, drinks_class):
    if drinks_type == "Hot":
        args = drinks_class.id
        sql_query = "DELETE FROM hot_drinks WHERE id=%s"  # %s prevents SQL injection!
        save_sql(sql_query, args)
        print(f"{drinks_class.drink_choice} was deleted")
    elif drinks_type == "Soft":
        args = drinks_class.id
        sql_query = "DELETE FROM soft_drinks WHERE id=%s"  # %s prevents SQL injection!
        save_sql(sql_query, args)
        print(f"{drinks_class.drink_choice} was deleted")
    elif drinks_type == "Alcy":
        args = drinks_class.id
        sql_query = "DELETE FROM alcoholic_drinks WHERE id=%s"  # %s prevents SQL injection!
        save_sql(sql_query, args)
        print(f"{drinks_class.drink_choice} was deleted")
    else:
        return


# def update_sql(self, sql_string, args):
#     connection = self.get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute(sql_string, args)
#     connection.commit()
#     connection.close()
#
#
# def sql_load_all(self, sql_string):
#     connection = self.get_connection()
#     sql_load_list = []
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute(sql_string)
#         connection.commit()
#         while True:
#             row = cursor.fetchone()
#             if row == None:
#                 break
#             else:
#                 sql_load_list.append(row)
#         return(sql_load_list)
#     except Exception as error:
#         print(f"Unable to return all: \n{error}")
#     finally:
#         connection.close()



