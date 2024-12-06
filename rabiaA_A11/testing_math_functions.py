import unittest
from math_functions import power, divide

class TestMathFunctions(unittest.TestCase):

    # Power function tests
    def test_power_positive(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(4, -1), 0.25)

    # Divide function tests
    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()

