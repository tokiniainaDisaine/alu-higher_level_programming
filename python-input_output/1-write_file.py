#!/usr/bin/python3
"""
This module writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    This funcition writes a string to a text file (UTF8)
    and returns the number of characters written:
    """

    with open(filename, 'w') as file:
        file.write(text)
    return len(text)