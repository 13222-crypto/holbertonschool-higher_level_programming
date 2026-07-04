#!/usr/bin/python3
"""
This module provides functions to serialize a Python dictionary into an
XML file and deserialize an XML file back into a Python dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary containing data to serialize.
        filename (str): The filename of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a Python dictionary.

    Args:
        filename (str): The filename of the input XML file.

    Returns:
        dict: A Python dictionary containing the deserialized data.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary from child elements
        return {child.tag: child.text for child in root}
    except Exception:
        return None
