#!/usr/bin/python3
"""
This module provides a function to save an object into a JSON file.
It encapsulates Python's built-in json writing capabilities.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The Python object data structure to serialize.
        filename (str): The path or name of the destination file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
