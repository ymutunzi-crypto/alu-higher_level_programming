#!/usr/bin/python3
"""Module that defines a Square class with an area method"""


class Square:
    """Class that defines a square and calculates its area"""

    def __init__(self, size=0):
        """Initializes the square with validation
        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the current square area
        Returns:
            The square of the size
        """
        return self.__size ** 2
