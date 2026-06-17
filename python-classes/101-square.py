#!/usr/bin/python3
"""
This module defines a class Square with private attributes size and position,
supporting property getters/setters, area, custom printing, and string representation.
"""


class Square:
    """
    A class that defines a square by its size and position, and allows
    direct string representation for printing.

    Attributes:
        __size (int): The size of a side of the square (private).
        __position (tuple): The position coordinates of the square (private).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the side of the square. Defaults to 0.
            position (tuple): Two positive integers representing coordinates.
        """
        self.size = size
        self.position = position

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
        Sets the private size attribute with validations.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the private position attribute.

        Returns:
            tuple: Two positive integers representing coordinates.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the private position attribute with validations.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square in stdout with '#' factoring in position coordinates.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Defines the printable string representation of a Square instance.
        Matches the exact output configuration of my_print().

        Returns:
            str: The text representation of the square.
        """
        square_str = ""
        if self.__size == 0:
            return square_str

        # إضافة الأسطر الفارغة العلوية
        for _ in range(self.__position[1]):
            square_str += "\n"

        # بناء أسطر المربع بالمسافات والرموز
        for i in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                square_str += "\n"

        return square_str
