#!/usr/bin/python3
"""
This module defines a custom list subclass named VerboseList.
It provides automatic descriptive notifications for modifying actions.
"""


class VerboseList(list):
    """
    A list subclass that outputs explicit notifications during transformations.
    """

    def append(self, item):
        """
        Appends an element to the list and displays a notification.

        Args:
            item (any): The data entity to insert at the end.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """
        Extends the list with multiple items and displays a notification.

        Args:
            x (iterable): The collection of entities to append.
        """
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """
        Removes a specific item and prints an early notification.

        Args:
            item (any): The targeted data value to delete.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Pops an item out of the list and prints an early notification.

        Args:
            index (int): The position index of the element, defaults to -1.

        Returns:
            any: The item removed from the specified position.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
