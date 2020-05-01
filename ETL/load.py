# Load

from src.ETL.customerclass import Customer
from src import persistence as perdb


def load_customers():
    connection = perdb.get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customer")
    customers = []

    while True:
        row = cursor.fetchone()
        if row == None:
            break
        customer = Customer(row[1],row[2],row[3],row[4],row[5],row[0])
        customers.append(customer)

    cursor.close()
    connection.close()
    return customers


def save_to_db(customers):
    connection = perdb.get_connection()
    cursor = connection.cursor()
    for customer in customers:
        try:
            cursor.execute("""INSERT INTO people (drinker_first_name, drinker_surname, drinker_age) 
                VALUES (%s, %s, %s)""", customer)
        except Exception as error:
            print(error)
    connection.commit()
    cursor.close()
    connection.close()