#!/usr/bin/python3
"""
This module provides a function to add two numbers.
The function ensures that the arguments are either integers or floats,
casts them to integers if necessary, and returns their sum.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float, defaults to 98).

    Raises:
        TypeError: If a or b is not an integer or a float,
                   or if they are NaN or Infinity.

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # الحماية من قيم NaN و Infinity لأنها لا تحول إلى int
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
