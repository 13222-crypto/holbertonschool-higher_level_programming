#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
It provides validation, area computation, and customized string output.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A full representation of a rectangle shape derived from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with strict bounds validation.

        Args:
            width (int): The quantitative width of the rectangle.
            height (int): The quantitative height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes and returns the area of the rectangle instance.

        Returns:
            int: The calculated area value.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a customized string representation of the Rectangle instance.

        Returns:
            str: A formatted string describing the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
