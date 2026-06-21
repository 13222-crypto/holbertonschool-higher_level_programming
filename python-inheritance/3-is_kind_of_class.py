#!/usr/bin/python3
"""
This module provides a flexible type evaluation function.
It checks both direct instantiation and hierarchical inheritance.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj (any): The object to evaluate.
        a_class (type): The target class type to verify against.

    Returns:
        bool: True if the object belongs to the class or its lineage,
              otherwise False.
    """
    return isinstance(obj, a_class)
