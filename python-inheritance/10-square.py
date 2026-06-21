#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
It models a perfect square geometry through specialized rectangle parameters.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A representation of a square shape derived from Rectangle blueprints.
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
