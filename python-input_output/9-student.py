#!/usr/bin/python3
"""
This module defines a Student class with basic attributes
and a method to convert the instance to a JSON dictionary.
"""


class Student:
    """
    Represents a student with personal details.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: The dictionary representation of the attributes.
        """
        return self.__dict__
