#!/usr/bin/python3
import unittest
from advanced.calculator import Calculator


class CalculatorTests(unittest.TestCase):
    """Unit tests for the Calculator class."""

    def setUp(self):
        """_summary_
        """
        self.calculator = Calculator()

    def test_addition(self):
        """
        Test addition operation of the Calculator class.
        """
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_subtraction(self):
        """
        Test subtraction operation of the Calculator class.
        """
        self.assertEqual(self.calculator.subtract(5, 2), 3)

    def test_multiplication(self):
        """
        Test multiplication operation of the Calculator class.
        """
        self.assertEqual(self.calculator.multiply(4, 3), 12)

    def test_division(self):
        """
        Test division operation of the Calculator class.
        """
        self.assertEqual(self.calculator.divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)

    def test_large_numbers(self):
        """
        Test calculation with large numbers.
        """
        result = self.calculator.add(123456789, 987654321)
        self.assertEqual(result, 1111111110)

    def test_negative_numbers(self):
        """
        Test calculation with negative numbers.
        """
        result = self.calculator.multiply(-5, 2)
        self.assertEqual(result, -10)

    def test_decimal_numbers(self):
        """
        Test calculation with decimal numbers.
        """
        result = self.calculator.divide(10.5, 2)
        self.assertAlmostEqual(result, 5.25, places=2)

    def test_zero_result(self):
        """
        Test calculation resulting in zero.
        """
        result = self.calculator.subtract(5, 5)
        self.assertEqual(result, 0)
