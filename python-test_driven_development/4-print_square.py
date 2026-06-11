#!/usr/bin/python3
"""
This module provides a function that prints a square.
The square is printed using the '#' character based on a given size.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size: The size length of the square (must be an integer).

    Raises:
        TypeError: If size is not an integer, or if it is a float less than 0.
        ValueError: If size is an integer less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
