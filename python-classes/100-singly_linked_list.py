#!/usr/bin/python3
"""
This module defines a Node class and a SinglyLinkedList class
to implement a sorted singly linked list in Python.
"""


class Node:
    """
    Defines a node of a singly linked list.

    Attributes:
        __data (int): The data stored within the node (private).
        __next_node (Node): The next node in the list (private).
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The data for the node.
            next_node (Node): The next node in the sequence. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.

        Returns:
            int: The node's data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node with validations.

        Args:
            value (int): The new integer value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node reference.

        Returns:
            Node: The next node or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node reference with validations.

        Args:
            value (Node): The next node object or None.

        Raises:
            TypeError: If value is neither None nor a Node instance.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list with sorted insertion capabilities.

    Attributes:
        __head (Node): The beginning node of the list (private).
    """

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """
        Defines the string representation of the list for printing.
        Each node data is printed on a new line.

        Returns:
            str: The formatted contents of the list.
        """
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position (increasing order).

        Args:
            value (int): The integer value to insert.
        """
        new_node = Node(value)

        # الحالة 1: القائمة فارغة أو القيمة الجديدة أصغر من رأس القائمة (Head)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # الحالة 2: البحث عن المكان الصحيح للإدراج في منتصف أو نهاية القائمة
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
