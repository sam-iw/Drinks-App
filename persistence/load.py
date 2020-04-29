import csv
import pymysql
from os import environ
from persistence.database import Person

def load_dictionary(filepath, dictionary):
    try:
        with open(filepath, "r") as dictionary_file:
            dictionary_lines = dictionary_file.readlines()
            for line in dictionary_lines:
                key_value_pair = line.split(': ')
                key = key_value_pair[0]
                value = key_value_pair[1].strip("\n")
                dictionary[key] = value
    except:
        print("oh no, an error occured, please select next option: ")
        count = 1
    for key, value in dictionary.items():
        print(f" |  {count}. {key}'s drink of choice is {value}")
        count += 1


def load_csv_dictionary(filepath, dictionary):
    try:
        with open(filepath, "r") as csvfile:
            line = csv.reader(csvfile, quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in line:
                key = row[0]
                value = row[1]
                dictionary[key] = value
    except:
        print("oh no, an error occured, please select next option: ")



def load_hot_drinks_prefs(filepath, dictionary):
    try:
        with open(filepath, "r") as csvfile:
            line = csv.reader(csvfile, quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in line:
                person = row[0]
                hot_drink_choice = row[1]
                hot_drink_milk = row[2]
                hot_drink_strength = row[3]
                hot_drink_sugar = row[4]
                dictionary[person] = [hot_drink_choice, hot_drink_milk, hot_drink_strength, hot_drink_sugar]
    except:
        print("oh no, an error occured, please select next option: ")


def load_lists(filename, lst):
    # try:
    with open(filename, 'r') as file:
        for item in file.readlines():
            item = item.strip()
            lst.append(item)
    # except Exception as err:
    #     print('Something went wrong ' + str(err))


def get_connection(): # function to get the connection string using: pymysql.connect(host, username, password, database)
    db_connection = pymysql.connect(
        environ.get('DB_HOST'), #host
        environ.get('DB_USER'), #username
        environ.get('DB_PW'), #password
        environ.get('DB_NAME') #database
        )
    print("Connection with DB established, get in")
    return db_connection


def load(tables):
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
            tables = (row[1], row[2], row[0])  # row 0 last because it's a default
        elif tables == "soft_drinks":
            tables = (row[1], row[0])  # row 0 last because it's a default
        elif tables == "alcoholic_drinks":
            tables = (row[1], row[0])  # row 0 last because it's a default
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





people = []
# get_connection().load("people")
# print(people)