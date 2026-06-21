#!/usr/bin/python3
"""
This module demonstrates Object-Oriented Programming using Abstract Base Classes.
It establishes a rigorous blueprint for animal sound behaviors.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract base class representing a generic animal contract.
    """

    @abstractmethod
    def sound(self):
        """
        An abstract method that must be overridden by all animal subclasses.
        """
        pass


class Dog(Animal):
    """
    A concrete subclass representing a dog derived from Animal.
    """

    def sound(self):
        """
        Implements the mandatory sound contract for a dog instance.

        Returns:
            str: The vocalization string "Bark".
        """
        return "Bark"


class Cat(Animal):
    """
    A concrete subclass representing a cat derived from Animal.
    """

    def sound(self):
        """
        Implements the mandatory sound contract for a cat instance.

        Returns:
            str: The vocalization string "Meow".
        """
        return "Meow"
