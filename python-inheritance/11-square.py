#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
It provides validation, area computation, and a custom string conversion.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A representation of a square shape derived from Rectangle mechanics.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with defensive validation.

        Args:
            size (int): The positive quantitative size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a customized string representation of the Square instance.

        Returns:
            str: A formatted string describing the square parameters.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
