#!/usr/bin/python3
"""
This module defines a custom iterator subclass named CountedIterator.
It tracks and monitors the absolute count of items processed during iteration.
"""


class CountedIterator:
    """
    An iterator wrapper that keeps a precise runtime count of elements fetched.
    """

    def __init__(self, some_iterable):
        """
        Initializes the CountedIterator instance.

        Args:
            some_iterable (iterable): The data collection to iterate over.
        """
        self.__iterator = iter(some_iterable)
        self.__counter = 0

    def get_count(self):
        """
        Retrieves the exact number of elements iterated so far.

        Returns:
            int: The current state of the internal counter.
        """
        return self.__counter

    def __next__(self):
        """
        Fetches the next element from the iterator and increments the counter.

        Raises:
            StopIteration: If there are no further items remaining.

        Returns:
            any: The next data entity from the sequence.
        """
        try:
            item = next(self.__iterator)
            self.__counter += 1
            return item
        except StopIteration:
            raise StopIteration
