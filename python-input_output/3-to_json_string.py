#!/usr/bin/python3
"""
This module provides a function to serialize an object into a JSON string.
It encapsulates Python's built-in json conversion capabilities.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The Python object data structure to be converted.

    Returns:
        str: The serialized JSON string representation of the object.
    """
    return json.dumps(my_obj)
