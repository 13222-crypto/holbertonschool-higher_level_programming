#!/usr/bin/python3
"""
This module defines a rebel integer class named MyInt.
It purposely inverts the behavior of equality and inequality operators.
"""


class MyInt(int):
    """
    A rebellious integer class that swaps the outcomes of == and !=.
    """

    def __eq__(self, other):
        """
        Overrides the standard equality operator to act as inequality.

        Args:
            other (any): The second value to compare against.

        Returns:
            bool: True if values are not equal, False if they are equal.
        """
        return int(self) != other

    def __ne__(self, other):
        """
        Overrides the standard inequality operator to act as equality.

        Args:
            other (any): The second value to compare against.

        Returns:
            bool: True if values are equal, False if they are not equal.
        """
        return int(self) == other
