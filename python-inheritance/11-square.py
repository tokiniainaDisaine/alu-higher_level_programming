#!/usr/bin/python3
"""This modules uses inheritance"""

class Square(Rectangle):

    def __init__(self, size):
        super.__init__(size, size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__width, self.__height)
