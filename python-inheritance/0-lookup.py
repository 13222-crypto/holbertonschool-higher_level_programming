#!/usr/bin/python3
"""
This module contains a function that inspects an object.
It provides a way to see all available properties and behaviors.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (any): The object to be inspected.

    Returns:
        list: A list of strings representing attributes and methods.
    """
    return dir(obj)
