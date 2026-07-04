#!/usr/bin/python3
"""
This module provides a function to return the dictionary description
of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    return obj.__dict__
