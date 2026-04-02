#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an integer validator.
"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an Exception for unimplemented area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
