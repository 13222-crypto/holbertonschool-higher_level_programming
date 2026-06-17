#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size,
area calculation, and support for comparison operators based on area.
"""


class Square:
    """
    A class that defines a square by its size and allows comparisons
    between squares based on their area.

    Attributes:
        __size (int or float): The size of a side of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int or float): The size of the side of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the private size attribute.

        Returns:
            int or float: The size of the square side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the private size attribute with float and int validations.

        Args:
            value (int or float): The new size value.

        Raises:
            TypeError: If value is not an integer or a float.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current square area.

        Returns:
            int or float: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Compares if two squares are equal in area (==)."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares if two squares are not equal in area (!=)."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compares if this square's area is less than the other (<)."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compares if this square's area is less than or equal (<=)."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compares if this square's area is greater than the other (>)."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compares if this square's area is greater than or equal (>=)."""
        return self.area() >= other.area()
