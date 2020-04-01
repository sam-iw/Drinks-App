import csv


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


def load_csv_dictionary(filepath,dictionary):
    try:
        with open(filepath, "r") as csvfile:
            csv_file = csv.reader(csvfile)
            for line in csv_file:
                key = line[0]
                value = line[1]
                dictionary[key] = value
    except:
        print("oh no, an error occured, please select next option: ")
    count = 1
    for key, value in dictionary.items():
        print(f" |  {count}. {key}'s drink of choice is {value}")
        count += 1


def load_lists(filename, lst):
    try:
        with open(filename, 'r') as file:
            for item in file.readlines():
                item = item.strip()
                lst.append(item)
    except Exception as err:
        print('Something went wrong ' + str(err))