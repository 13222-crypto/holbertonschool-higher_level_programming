#!/usr/bin/python3
"""
This module demonstrates the application of Mixins in Python.
It constructs standalone capability injectors to enhance the Dragon class.
"""


class SwimMixin:
    """
    A mixin that provides swimming functionality to any incorporating creature.
    """

    def swim(self):
        """
        Prints a generic swimming notification message.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin that provides flying functionality to any incorporating creature.
    """

    def fly(self):
        """
        Prints a generic flying notification message.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A comprehensive class representing a mystical Dragon.
    It composes swimming and flying behaviors via multiple mixin components.
    """

    def roar(self):
        """
        Prints an explicit dragon roaring vocalization statement.
        """
        print("The dragon roars!")
