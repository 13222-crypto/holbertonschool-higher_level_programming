#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size.
It introduces the concept of data encapsulation in Python.
"""


class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The size of a side of the square (private).
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the side of the new square.
        """
        self.__size = size
