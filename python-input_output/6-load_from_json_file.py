#!/usr/bin/python3
"""
This module provides a function to load an object from a JSON file.
It encapsulates Python's built-in json reading capabilities.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): The path or name of the source JSON file.

    Returns:
        any: The Python data structure created from the JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
