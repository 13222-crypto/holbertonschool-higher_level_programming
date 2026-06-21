#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
It encapsulates dimensions and applies geometry validation constraints.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A representation of a rectangle shape derived from geometry foundations.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with strict bounds.

        Args:
            width (int): The positive quantitative width of the rectangle.
            height (int): The positive quantitative height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
