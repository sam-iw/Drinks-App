def print_hot_dicts(dict):
    for key, value in dict.items():
        print(f"{key}'s hot drink is {value[0]}, {value[1]}, {value[2]}, with {value[3]} sugar(s)")


def print_soft_or_alcy_dicts(dict):
    for key, value in dict.items():
        print(f"{key}'s preferred drink is {value}")


def print_hot_drinks(list):
    for item in list:
        print(f"{item.drink_choice}, {item.milk_choice}, {item.strength_choice}, with {item.sugar_choice} sugar(s)")


def print_soft_or_alcy_drinks(list):
    for item in list:
        print(f"{item.drink_choice}, {item.drink_quantity}ml")


def print_person(list):
    for item in list:
        print(f"{item.first_name} {item.surname} is {item.age}")

