#!/usr/bin/python3
"""This module shows inheritance"""


class Rectangle(BaseGeometry):
    """This is a rectangle class"""

    def __init__(self, width, height):
        """This is the instantiator function"""
        self.__width = integer_validator("width", width)
        self.__height = integer_validator("height", height)
    
    def __str__(self):
        print("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        """This function returns the area of a rectangle"""

        return self.__width * self.__height
