#!/usr/bin/python3
"""
This module defines geometric structures using Abstract Base Classes.
It demonstrates Duck Typing by uniformly interacting with distinct shapes.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    An abstract base class acting as an interface blueprint for shapes.
    """

    @abstractmethod
    def area(self):
        """
        Computes the mathematical area of the shape instance.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Computes the mathematical perimeter of the shape instance.
        """
        pass


class Circle(Shape):
    """
    A concrete implementation of a circular geometry.
    """

    def __init__(self, radius):
        """
        Initializes a new Circle instance.

        Args:
            radius (int, float): The radial reach from the center.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the explicit area of the circle.

        Returns:
            float: Total surface area.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates the explicit perimeter or circumference of the circle.

        Returns:
            float: Total outer boundary length.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    A concrete implementation of a rectangular geometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, float): The structural width of the shape.
            height (int, float): The structural height of the shape.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the explicit area of the rectangle.

        Returns:
            int, float: Total internal surface units.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the explicit perimeter of the rectangle.

        Returns:
            int, float: Combined outer edges length.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Leverages Duck Typing to report metrics of any compliant shape object.

    Args:
        shape (Shape): An object adhering to the Shape method interface.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
