#!/usr/bin/python3
"""
This module demonstrates multiple inheritance in Python.
It defines Fish and Bird parent classes, and a FlyingFish subclass.
"""


class Fish:
    """
    A class representing fish behaviors and habitats.
    """

    def swim(self):
        """
        Prints the swimming behavior of a standard fish.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints the typical environment where fish reside.
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing bird behaviors and habitats.
    """

    def fly(self):
        """
        Prints the flying behavior of a standard bird.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints the typical environment where birds reside.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A subclass inheriting from both Fish and Bird demonstrating MRO.
    """

    def fly(self):
        """
        Overrides the fly method specifically for the flying fish.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Overrides the swim method specifically for the flying fish.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Overrides the habitat method to reflect the multi-environment nature.
        """
        print("The flying fish lives both in water and the sky!")
