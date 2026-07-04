#!/usr/bin/python3
"""
This module provides a function for writing text data into files.
It demonstrates basic file writing operations with explicit character counting.
"""


def write_file(filename="", text=""):
    """
    Writes a given string to a UTF-8 text file and returns characters written.

    Args:
        filename (str): The path or name of the file. Defaults to "".
        text (str): The text content to write inside the file. Defaults to "".

    Returns:
        int: The total number of characters successfully written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
