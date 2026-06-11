#!/usr/bin/python3
"""
Unittest for max_integer([..])
This module contains unit tests to cover all edge cases
for the max_integer function.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unit tests for the max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_no_arguments(self):
        """Test with no arguments passed (uses default empty list)."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test with a single element in the list."""
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative(self):
        """Test with a list containing only negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_negative_positive(self):
        """Test with a list containing both negative and positive numbers."""
        self.assertEqual(max_integer([-10, 5, -3, 0, 4]), 5)

    def test_max_at_the_beginning(self):
        """Test where the maximum value is at the start of the list."""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_floats(self):
        """Test with a list containing float values."""
        self.assertEqual(max_integer([1.53, 6.33, -2.5, 4.2]), 6.33)

    def test_mixed_ints_and_floats(self):
        """Test with a list containing both integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 0.5]), 3)


if __name__ == '__main__':
    unittest.main()
