#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size,
including its getter and setter properties, and an area method.
"""


class Square:
    """
    A class that defines a square by its size, with encapsulation
    using property getters and setters.

    Attributes:
        __size (int): The size of a side of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the side of the new square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the private size attribute.

        Returns:
            int: The size of the square side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the private size attribute with proper type and value validations.

        Args:
            value (int): The new size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current square area.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
