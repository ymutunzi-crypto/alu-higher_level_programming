#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A class with area and integer validation"""

    def area(self):
        """Raises an Exception because it is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value: must be an integer and > 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
