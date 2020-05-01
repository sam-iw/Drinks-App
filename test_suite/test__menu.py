import MainApp as app
import unittest.mock
from persistence.database import Person
from unittest.mock import Mock


class TestMenu(unittest.TestCase):

    @unittest.mock.patch("MainApp.initial_function")
    @unittest.mock.patch("builtins.input", return_value=unittest.mock)
    @unittest.mock.patch('os.system')
    def test_initial_options(self, system, mock_input, initial_function):
        #Arrange
        mock_input.side_effect = ["1"]

        #Act
        app.initial_options()

        #Assert
        system.assert_called_once_with("Clear")
        initial_function.assert_called_once_with("1")

    @unittest.mock.patch("MainApp.s1_search_people")
    def test_initial_function(self, s1_search_people):
        #Arrange

        #Act
        app.initial_function("1")

        #Assert
        s1_search_people.assert_called_once()

    @unittest.mock.patch("MainApp.s2_search_drinks")
    def test_initial_function_o2(self, s2_search_drinks):
        #Arrange

        #Act
        app.initial_function("2")

        #Assert
        s2_search_drinks.assert_called_once()

    @unittest.mock.patch("MainApp.s9_round_type")
    def test_initial_function_o9(self, s9_round_type):
        # Arrange

        # Act
        app.initial_function("9")

        # Assert
        s9_round_type.assert_called_once()

    @unittest.mock.patch("MainApp.s3_create_person")
    def test_initial_function_o3(self, s3_create_person):
        #Arrange

        #Act
        app.initial_function("3")

        #Assert
        s3_create_person.assert_called_once()

    @unittest.mock.patch("MainApp.s4_add_drinks")
    def test_initial_function_o4(self, s4_add_drinks):
        # Arrange

        # Act
        app.initial_function("4")

        # Assert
        s4_add_drinks.assert_called_once()

    @unittest.mock.patch("MainApp.s5_delete_person")
    def test_initial_function_o5(self, s5_delete_person):
        # Arrange

        # Act
        app.initial_function("5")

        # Assert
        s5_delete_person.assert_called_once()

    @unittest.mock.patch("MainApp.s6_delete_drinks_type")
    def test_initial_function_o6(self, s6_delete_drinks_type):
        # Arrange

        # Act
        app.initial_function("6")

        # Assert
        s6_delete_drinks_type.assert_called_once()

    @unittest.mock.patch("MainApp.s8_print_functions")
    def test_initial_function_o8(self, s8_print_functions):
        # Arrange

        # Act
        app.initial_function("8")

        # Assert
        s8_print_functions.assert_called_once()

    @unittest.mock.patch("MainApp.s7_drinks_pref_menu")
    def test_initial_function_o7(self, s7_drinks_pref_menu):
        # Arrange

        # Act
        app.initial_function("7")

        # Assert
        s7_drinks_pref_menu.assert_called_once()

    @unittest.mock.patch("builtins.input", return_value=unittest.mock)
    @unittest.mock.patch("MainApp.initial_options")
    def test_nav_options_o1(self, initial_options, mock_input):
        # Arrange
        mock_input.side_effect = ["1"]

        # Act
        app.sn_nav_options()

        # Assert
        initial_options.assert_called_once()


if __name__ == "__main__":
    unittest.main()



