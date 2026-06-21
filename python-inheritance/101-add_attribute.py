#!/usr/bin/python3
"""
This module provides defensive attribute injection utilities.
It checks structural expandability before modifying object instances.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if execution is possible.

    Args:
        obj (any): The target instance object to modify.
        name (str): The string identifier name of the attribute.
        value (any): The payload value to link with the attribute.

    Raises:
        TypeError: If the target object lacks a dictionary configuration.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
