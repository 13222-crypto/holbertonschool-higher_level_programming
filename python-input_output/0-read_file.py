#!/usr/bin/python3
"""
This module contains a function that reads and prints a text file.
It demonstrates standard file input operations using the with statement.
"""


def read_file(filename=""):
    """
    Reads a text file encoded in UTF-8 and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read. Defaults to "".
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
