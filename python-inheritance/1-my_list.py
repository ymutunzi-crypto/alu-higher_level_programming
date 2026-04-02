#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A class that inherits from list and adds a custom sorting method.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))
