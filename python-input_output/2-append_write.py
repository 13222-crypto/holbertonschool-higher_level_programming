#!/usr/bin/python3
"""
This module provides a function for appending text data onto files.
It demonstrates basic file appending operations.
"""


def append_write(filename="", text=""):
    """
    Appends a given string to a UTF-8 text file and returns characters added.

    Args:
        filename (str): The path or name of the file. Defaults to "".
        text (str): The text content to append to the file. Defaults to "".

    Returns:
        int: The total number of characters successfully added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
