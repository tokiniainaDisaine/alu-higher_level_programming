#!/usr/bin/python3
"""This modules uses inheritance"""
Rectangle = __import__("7-base_geometry").Rectangle


class Square(Rectangle):

    def __init__(self, size):
        super.__init__(size, size)
