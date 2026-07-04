#!/usr/bin/python3
"""
This module provides a function to convert data from a CSV file
into a JSON file format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file named data.json.

    Args:
        csv_filename (str): The filename of the input CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        data = []
        with open(csv_filename, 'r', encoding='utf-8') as csv_f:
            reader = csv.DictReader(csv_f)
            for row in reader:
                data.append(row)

        with open('data.json', 'w', encoding='utf-8') as json_f:
            json.dump(data, json_f, indent=4)

        return True
    except Exception:
        return False
