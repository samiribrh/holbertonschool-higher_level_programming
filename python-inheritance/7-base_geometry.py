#!/usr/bin/python3
"""Module containing BaseGeometry class"""


class BaseGeometry:
    """Class for BaseGeometry"""

    def area(self):
        """Method to raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate value"""

        # Checking if value is not an int
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")

        # Checking if value is not less or equal to 0
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
