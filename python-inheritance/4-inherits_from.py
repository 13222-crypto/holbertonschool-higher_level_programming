#!/usr/bin/python3
"""
This module provides a strict subclass validation function.
It isolates objects derived from subclassing rather than original types.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class inherited from a_class.

    Args:
        obj (any): The object to evaluate.
        a_class (type): The base class type to check against.

    Returns:
        bool: True if the object's class is a strict subclass of a_class,
              otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
