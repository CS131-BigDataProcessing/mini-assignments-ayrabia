import unittest
import pandas as pd
from validate_functions import validate_data
from stats_function import calculate_stats

class TestCrimeTest(unittest.TestCase):

    def test_validate_data(self):
        # Valid data
        valid_data = pd.DataFrame({'Vict sex': ['M', 'F'], 'Vict age': [25, 30]})
        self.assertTrue(validate_data(valid_data))

        # Invalid data (wrong values)
        invalid_data = pd.DataFrame({'Vict sex': ['X'], 'Vict age': [101]})
        self.assertFalse(validate_data(invalid_data))

        # Invalid data (NULL values)
        null_data = pd.DataFrame({'Vict sex': [None], 'Vict age': [50]})
        self.assertFalse(validate_data(null_data))

    def test_calculate_stats(self):
        data = pd.DataFrame({'Vict age': [10, 20, 30, 40]})
        mean, median = calculate_stats(data)
        self.assertEqual(mean, 25)
        self.assertEqual(median, 25)

if __name__ == '__main__':
    unittest.main()

