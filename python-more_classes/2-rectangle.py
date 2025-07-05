#!/usr/bin/python3
"""This is a rectangle class that does nothing"""


class Rectangle:
    """This is a rectangle class that stores a size and can calculate the area"""

    def __init__(self, width=0, height=0):
        """This function initializes the class"""
        
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This function returns the value of width"""

        return self.__width

    @width.setter
    def size(self, value):
        """This function allows you to change the value of width"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This function returns the value of height"""

        return self.__height

    @height.setter
    def size(self, value):
        """This function allows you to change the value of height"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (self.__height + self.__width) * 2
