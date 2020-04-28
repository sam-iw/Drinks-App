from persistence.database import save_people, delete_person, save_drinks, delete_drinks, Person, HotDrinks, SoftDrinks, AlcyDrinks
import unittest.mock
from unittest.mock import Mock


class Test_app(unittest.TestCase):

    @unittest.mock.patch("persistence.database.save_sql", return_value=unittest.mock)
    def test_save_people(self, m_save_sql):
        # arrange
        mock_person = Mock(Person)
        mock_person.first_name = "Testy"
        mock_person.surname = "McTest"
        mock_person.age = 22
        mock_person.id = None
        # act
        save_people(mock_person)
        # assert
        m_save_sql.assert_called_once_with("INSERT INTO people (drinker_first_name, drinker_surname, drinker_age) VALUES (%s, %s, %s)",
                                           ("Testy", "McTest", 22))

    @unittest.mock.patch("persistence.database.save_sql", return_value=unittest.mock)
    def test_save_hot_drinks(self, m_save_sql):
        #arrange
        mock_hot_drinks = Mock(HotDrinks)
        mock_hot_drinks.drink_choice = "Test Tea"
        mock_hot_drinks.milk_choice = "Test White"
        mock_hot_drinks.strength_choice = "Test Mild"
        mock_hot_drinks.sugar_choice = 0
        mock_hot_drinks.id = None

        #act
        save_drinks([mock_hot_drinks], "Hot")

        #assert
        m_save_sql.assert_called_once_with("INSERT INTO hot_drinks (hot_drink, milk, drink_strength, sugar) VALUES (%s, %s, %s, %s)",
                                           ("Test Tea", "Test White", "Test Mild", 0))

    @unittest.mock.patch("persistence.database.save_sql", return_value=unittest.mock)
    def test_save_soft_drinks(self, m_save_sql):
        #arrange
        mock_soft_drinks = Mock(SoftDrinks)
        mock_soft_drinks.drink_choice = "Test Coke"
        mock_soft_drinks.drink_quantity = 330
        mock_soft_drinks.id = None

        #act
        save_drinks([mock_soft_drinks], "Soft")

        #assert
        m_save_sql.assert_called_once_with("INSERT INTO soft_drinks (soft_drink, soft_quantity_ml) VALUES (%s, %s)",
                                           ("Test Coke", 330))

    @unittest.mock.patch("persistence.database.save_sql", return_value=unittest.mock)
    def test_save_alcoholic_drinks(self, m_save_sql):
        # arrange
        mock_alcy_drinks = Mock(AlcyDrinks)
        mock_alcy_drinks.drink_choice = "Test Lager"
        mock_alcy_drinks.drink_quantity = 568
        mock_alcy_drinks.id = None

        # act
        save_drinks([mock_alcy_drinks], "Alcy")

        # assert
        m_save_sql.assert_called_once_with("INSERT INTO alcoholic_drinks (alcy_drink, alcy_quantity_ml) VALUES (%s, %s)",
                                           ("Test Lager", 568))

    @unittest.mock.patch("persistence.database.save_sql", return_value=unittest.mock)
    def test_delete_people(self, m_save_sql):
        # arrange
        mock_person = Mock(Person)
        mock_person.first_name = "Testy"
        mock_person.surname = "McTest"
        mock_person.age = 22
        mock_person.id = 1
        # act
        delete_person(mock_person)
        # assert
        m_save_sql.assert_called_once_with("DELETE FROM people WHERE id=%s", 1)

    @unittest.mock.patch("persistence.database.save_sql", return_value=unittest.mock)
    def test_delete_hot_drinks(self, m_save_sql):
        # arrange
        mock_hot_drinks = Mock(HotDrinks)
        mock_hot_drinks.drink_choice = "Test Tea"
        mock_hot_drinks.milk_choice = "Test White"
        mock_hot_drinks.strength_choice = "Test Mild"
        mock_hot_drinks.sugar_choice = 0
        mock_hot_drinks.id = 1
        # act
        delete_drinks("Hot", mock_hot_drinks)
        # assert
        m_save_sql.assert_called_once_with("DELETE FROM hot_drinks WHERE id=%s", 1)

    @unittest.mock.patch("persistence.database.save_sql", return_value=unittest.mock)
    def test_delete_soft_drinks(self, m_save_sql):
        # arrange
        mock_soft_drinks = Mock(SoftDrinks)
        mock_soft_drinks.drink_choice = "Test Coke"
        mock_soft_drinks.drink_quantity = 330
        mock_soft_drinks.id = 1
        # act
        delete_drinks("Soft", mock_soft_drinks)
        # assert
        m_save_sql.assert_called_once_with("DELETE FROM soft_drinks WHERE id=%s", 1)

    @unittest.mock.patch("persistence.database.save_sql", return_value=unittest.mock)
    def test_delete_alcoholic_drinks(self, m_save_sql):
        # arrange
        mock_alcy_drinks = Mock(AlcyDrinks)
        mock_alcy_drinks.drink_choice = "Test Lager"
        mock_alcy_drinks.drink_quantity = 568
        mock_alcy_drinks.id = 1
        # act
        delete_drinks("Alcy", mock_alcy_drinks)
        # assert
        m_save_sql.assert_called_once_with("DELETE FROM alcoholic_drinks WHERE id=%s", 1)



if __name__ == "__main__":
    unittest.main()

