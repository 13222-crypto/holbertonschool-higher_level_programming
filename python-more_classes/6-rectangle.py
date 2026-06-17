#!/usr/bin/python3
"""
This module defines a Rectangle class with private attributes,
validation properties, geometric methods, and instance tracking.
"""


class Rectangle:
    """
    Defines a rectangle by width and height, tracking the number of instances.

    Attributes:
        number_of_instances (int): Total number of active instances (class attr).
        __width (int): The width of the rectangle (instance attr).
        __height (int): The height of the rectangle (instance attr).
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance and increments instance count.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the private width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the private width attribute with validations.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the private height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the private height attribute with validations.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter, or 0 if either side is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a printable string representation of the rectangle using '#'.

        If width or height is 0, returns an empty string.

        Returns:
            str: Visual representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_lines = []
        for _ in range(self.__height):
            rect_lines.append("#" * self.__width)

        return "\n".join(rect_lines)

    def __repr__(self):
        """
        Returns a string representation to recreate a new instance with eval().

        Returns:
            str: Formal string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message upon deletion and decrements instance count.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
