import MainApp as app
import unittest.mock


class TestPrefs(unittest.TestCase):

    @unittest.mock.patch("builtins.input", return_value=unittest.mock)
    def test_add_soft_or_alcy_preference(self, mock_input):
        # Arrange
        test_preferences = {}
        mock_input.side_effect = ["Alex: Wine"]
        expected_outcome = {"Alex": "Wine"}
        # Act
        actual_outcome = app.s7b_add_soft_or_alcy_prefs(test_preferences)
        # Assert
        self.assertEqual(expected_outcome, actual_outcome)

    @unittest.mock.patch("builtins.input", return_value=unittest.mock)
    def test_add_hot_preference(self, mock_input):
        # Arrange
        mock_input.side_effect = ["Alex", "Coffee", "black", "strong", 0]
        expected_outcome = {'Alex': ['Coffee', 'black', 'strong', 0]}
        # Act
        actual_outcome = app.s7a_add_hot_drink_prefs()
        # Assert
        self.assertEqual(expected_outcome, actual_outcome)


if __name__ == "__main__":
    unittest.main()

