#!/usr/bin/python3
"""
This module defines a custom list class that handles specialized
sorting and printing capabilities.
"""


class MyList(list):
    """
    A custom list class that extends the built-in list type.
    """

    def print_sorted(self):
        """
        Prints all elements of the list sorted in ascending order.
        Assumes all elements within the instance are integers.
        """
        print(sorted(self))
