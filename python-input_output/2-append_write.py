#!/usr/bin/python3
"""
This module appends a string to a text file (UTF8)
and returns the number of characters written:
"""

def append_write(filename="", text=""):
    """
    This funcition appends a string to a text file (UTF8)
    and returns the number of characters written:
    """

    with open(filename, 'a') as file:
        file.write(text)
    return len(text)
