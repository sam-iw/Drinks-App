import DrinksApp20200404 as app
import unittest.mock


class Test_app(unittest.TestCase):

    @unittest.mock.patch("builtins.input", return_value=unittest.mock)
    def test_add_preference(self, mock_input):
        # Arrange
        test_preferences = {"Alex": "Wine"}
        mock_input.side_effect = ["Alex: Wine"]
        expected_outcome = {"Alex": "Wine"}
        print(f"expected outcome is {expected_outcome}")
        # Act
        actual_outcome = app.add_soft_or_alcy_prefs(test_preferences)
        print(f"Actual outcome is {actual_outcome}")
        # Assert
        self.assertEqual(expected_outcome, actual_outcome)

        # assert actual_outcome == expected_outcome, f"""
        # actual outcome = {actual_outcome}
        # expected outcome = {expected_outcome}"""
        # print("Passed the GDPR test")

    @unittest.mock.patch("DrinksApp20200404.initial_function")
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

    # def delete_inputs(List):
    #     os.system("Clear")
    #     print("Below is a list of items currently stored in the app, which would you like to delete?")
    #     perprint.print_list(List)
    #     Deletions = input("Enter what to delete: ")
    #     try:
    #         for Deletion in Deletions.split(", "):
    #             List.remove(Deletion)
    #         print("The remaining items stored in the app are below:")
    #         perprint.print_list(List)
    #         nav_options()
    #     except:
    #         print("You have made an invalid entry.")
    #         nav_options()
    @unittest.mock.patch("DrinksApp20200404.nav_options")
    @unittest.mock.patch("builtins.input", return_value=unittest.mock)
    @unittest.mock.patch("builtins.print", return_value=None)
    @unittest.mock.patch('os.system')
    def test_delete_list_input(self, system, mock_print, mock_input, nav_options_stub):
        # Arrange
        mock_input.side_effect = ["Sam, Jake"] # To delete
        test_list = ["Sam", "Jake", "John"]
        expected_list = ["John"]

        # Act
        app.delete_inputs(test_list)

        # Assert
        self.assertEqual(expected_list,test_list)
        system.assert_called_once_with("Clear")
        nav_options_stub.assert_called_once()
        mock_print.assert_called()


if __name__ == "__main__":
    unittest.main()



