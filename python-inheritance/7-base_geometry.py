#!/usr/bin/python3
"""This module has an empty class"""


class BaseGeometry:
    """This is a class that does practically nothing"""

    def area(self):
        """This function raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function check if the value is valid"""
  
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
   
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
# idk tbh
