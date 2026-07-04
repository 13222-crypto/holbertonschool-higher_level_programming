#!/usr/bin/python3
"""
This module defines a custom Python class that can serialize and
deserialize its own instances using the pickle module.
"""
import pickle


class CustomObject:
    """
    A custom object holding basic student/person data with serialization hooks.
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initializes the custom object attributes.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in a pre-defined format.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to a file.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance of CustomObject from a file.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, Exception):
            return None
