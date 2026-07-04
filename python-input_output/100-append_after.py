#!/usr/bin/python3
"""
This module defines a function that inserts a line of text into a file
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing
    a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to look for in each line.
        new_string (str): The string to insert after lines that match.
    """
    lines_buffer = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines_buffer.append(line)
            if search_string in line:
                lines_buffer.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines_buffer)
