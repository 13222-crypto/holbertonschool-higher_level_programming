#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size.
It includes type and value validation for the size attribute during instantiation.
"""


class Square:
    """
    A class that defines a square by its size with data validation.

    Attributes:
        __size (int): The size of a side of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the side of the new square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
