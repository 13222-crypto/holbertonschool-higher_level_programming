#!/usr/bin/python3
"""
This module provides a function to deserialize a JSON string into an object.
It encapsulates Python's built-in json parsing capabilities.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string representation to decode.

    Returns:
        any: The decoded Python object (e.g., dict, list).
    """
    return json.loads(my_str)
