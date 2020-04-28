import csv


def save_list(filename, lst):
    try:
        with open(filename, 'w') as file:
            for item in lst:
                file.write(item + '\n')
    except Exception as err:
        print('Something went wrong ' + str(err))


def save_csv_dictionary(filepath, dictionary):
    try:
        with open(filepath, "w") as csvfile:  # pass csv file to the csv.writer
            dictionary_file = csv.writer(csvfile, quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for data in dictionary.items():
                dictionary_file.writerow(data)
    except:
        print("An error occurred (sorry:CSV)")


def save_hot_drinks(filepath, dictionary):
    try:
        with open(filepath, "w") as csvfile:  # pass csv file to the csv.writer
            dictionary_file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for person, value in dictionary.items():
                dictionary_file.writerow([person, value[0], value[1], value[2], value[3]])
    except Exception as error:
        print(error)
        print("An error occurred (sorry:CSV)")


def save_dictionary(filepath, dictionary):
    try:
        with open(filepath, "w") as dictionary_file:
            for key, value in dictionary.items():  # key and values in dict two, dict_two.items()
                dictionary_file.write(key, value)  # add to the text file, saves it (I think)
    except:
        print("An error occurred (sorry:Dict)")


