#!/usr/bin/python3
"""Module that defines a Square class with size and position"""


class Square:
    """Class that defines a square with coordinates for printing"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square
        Args:
            size (int): The side length
            position (tuple): The x, y coordinates
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__size_pos

    @position.setter
    def position(self, value):
        """Setter for position with specific tuple validation"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size_pos = value

    def area(self):
        """Calculates area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # and uses position for offsets"""
        if self.__size == 0:
            print("")
            return

        # Handle vertical offset (y)
        [print("") for i in range(self.__size_pos[1])]

        # Handle horizontal offset (x) and grid
        for i in range(self.__size):
            print(" " * self.__size_pos[0] + "#" * self.__size)
