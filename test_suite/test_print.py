import unittest.mock
import persistence.print as prin
from unittest.mock import Mock


class TestPrint(unittest.TestCase):

    def test_print_list(self):
        # Arrange
        diction = {'Alex': ['Coffee', 'black', 'strong', 0]}
        expected_outcome = ['Alex', 'Coffee', 'black', 'strong', 0]

        # Act
        actual_outcome = prin.print_class_dict(diction)

        # Assert
        print(f"expected {expected_outcome}"
              f"actual {actual_outcome}")
        self.assertEqual(expected_outcome, actual_outcome)


if __name__ == "__main__":
    unittest.main()
