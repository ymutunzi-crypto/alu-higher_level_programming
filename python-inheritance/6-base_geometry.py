#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an area method.
"""


class BaseGeometry:
    """Class representing BaseGeometry with an unimplemented area method."""

    def area(self):
        """
        Public instance method that raises an Exception.
        """
        raise Exception("area() is not implemented")
