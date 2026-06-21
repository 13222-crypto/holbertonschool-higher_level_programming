#!/usr/bin/python3
"""
This module defines a geometry base class with placeholder methods.
It sets structural contracts for subsequent geometric shape derivations.
"""


class BaseGeometry:
    """
    A base class representing geometric utility blueprints.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: Always raises an Exception because the concrete
                       behavior must be defined by subclass implementations.
        """
        raise Exception("area() is not implemented")
