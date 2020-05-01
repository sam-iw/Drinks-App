                 Welcome to BrIW

** The BrIW app allows you to create and save people and drinks to your database, assign drinks preferences to peoples and generate rounds according to their preferences or how they feel on the day.

BrIW also has a built in function to stop day time drinking to comply with the bar's license, sorry guys. 
  
  
**To install BrIW please follow the instructions below:**

1. Open DrinksApp folder in a python interpreter such as Pycharm or Visual Studio (VS) Code.

2. To install the modules required to run the BrIW required the virtual environment (venv) to be running:
    - Within the interpreter terminal type "python3 -m venv venv" to create a new venv
    - Next type in "source venv/bin/activate" to activate the venv
    - Enter "pip3 install -r requirements.txt" to install the modules required for BrIW
    - You might have to upgrade pip to do so "pip install --upgrade pip"
    
3. To run BrIW to DrinksApp in terminal and type in "python3 MainApp.py"

The app has the the following functions:

[1] Search People List - search the db for people

[2] Search Drinks List - search the db for hot, cold or alcoholic drinks

[3] Add Person - add a person to db

[4] Add Drink - add a hot, cold or alcoholic drinks from the db

[5] Delete Person - delete a person from the db

[6] Delete Drinks - delete a hot, cold or alcoholic drinks from the db

[7] Choose Preferences - assign hot, cold or alcoholic preferences to people (in seperate csv files)

[8] Print Functions - print: people, hot, cold or alcoholic drinks lists from db and hot, cold or alcoholic preferences

[9] Take Round - round builder function allows you to create a round according to the saved preferences or alternatively what they fancy today. 

[10] Exit App - quit BrIW

How to contribute to the BrIW:

BrIW is still in the development stages so there are plently of improvements to be made

- The drink preferences need to be linked to the database, currently drinkers have a drink preferences saved for each of the three drink types in the form of a unique number.

- Further expansion of the test suite is required coverage is fairly limited particularly the round builder.

- More input formatting

- The file directory requires tidying up.

- Greater search functionality search by first and last name rather than either.



    **