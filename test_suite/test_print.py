import unittest.mock
from src import persistence as prin
import io
from src.persistence import HotDrinks, SoftDrinks, Person


class TestPrint(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hot_dicts(self, mock_stdout):
        # Arrange
        diction = {'Testy': ['Coffee', 'black', 'strong', 0]}
        expected_outcome = """Testy's hot drink is Coffee, black, strong, with 0 sugar(s)\n"""
        # Act
        prin.print_hot_dicts(diction)
        # Assert
        self.assertEqual(expected_outcome, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_soft_or_alcy_dicts(self, mock_stdout):
        # Arrange
        diction = {'Testy': 'Coke'}
        expected_outcome = """Testy's preferred drink is Coke\n"""
        # Act
        prin.print_soft_or_alcy_dicts(diction)
        # Assert
        self.assertEqual(expected_outcome, mock_stdout.getvalue())


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hot_drinks(self, mock_stdout):
        # Arrange
        list = [HotDrinks('Coffee', 'black', 'strong', '0')]
        expected_outcome = """Coffee, black, strong, with 0 sugar(s)\n"""
        # Act
        prin.print_hot_drinks(list)
        # Assert
        self.assertEqual(expected_outcome, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_soft_or_alcy_drinks(self, mock_stdout):
        # Arrange
        list = [SoftDrinks('Test Coke', '330')]
        expected_outcome = """Test Coke, 330ml\n"""
        # Act
        prin.print_soft_or_alcy_drinks(list)
        # Assert
        self.assertEqual(expected_outcome, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_person(self, mock_stdout):
        # Arrange
        list = [Person('Testy', 'McTest', '35')]
        expected_outcome = """Testy McTest is 35\n"""
        # Act
        prin.print_person(list)
        # Assert
        self.assertEqual(expected_outcome, mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
