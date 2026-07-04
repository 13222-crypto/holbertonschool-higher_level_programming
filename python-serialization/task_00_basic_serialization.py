#!/usr/bin/python3
"""
This module provides basic serialization and deserialization functions
to save Python dictionaries as JSON files and reload them.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a specified JSON file.
    If the file already exists, it will be replaced.

    Args:
        data (dict): A Python dictionary containing data to serialize.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a specified JSON file.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized JSON data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
