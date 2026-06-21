#!/usr/bin/python3
"""
This module provides a specific type checking function.
It evaluates exact class replication without inheritance overhead.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj (any): The object to evaluate.
        a_class (type): The target class type to check against.

    Returns:
        bool: True if type matches exactly, otherwise False.
    """
    return type(obj) is a_class
