#!/usr/bin/python3
"""
This module defines a geometry base class with data validation utilities.
It offers defensive programming tools to ensure geometric dimensions are sane.
"""


class BaseGeometry:
    """
    A base class managing structural geometry and boundary validations.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: Enforces subclass implementation requirements.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is a positive integer.

        Args:
            name (str): The logical label or identifier of the parameter.
            value (int): The quantitative value to inspect.

        Raises:
            TypeError: If the value provided is not a strict integer type.
            ValueError: If the value provided is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
