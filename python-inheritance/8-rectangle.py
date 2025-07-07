#!/usr/bin/python3
"""This module shows inheritance"""


class Rectangle(BaseGeometry):
    """This is a rectangle class"""

    def __init__(self, width, height):
        """This is the instantiator function"""
        self.__width = integer_validator("width", width)
        self.__height = integer_validator("height", height)
    