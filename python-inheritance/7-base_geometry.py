#!/usr/bin/python3
"""This module has an empty class"""


class BaseGeometry:
    """This is a class that does practically nothing"""

    def area(self):
        """This function raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function check if the value is valid"""
        if isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value < 0:
            raise ValueError("<name> must be greater than 0")
        else:
            return value
# idk tbh
