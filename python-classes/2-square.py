#!/usr/bin/python3
"""This is a square class that does nothing"""


class Square:
    """This is a square class that checks if the initial value is an integer"""

    def __init__(self, size=0):
        """This function checks if the argument is an integer"""

        if size < 0:
            raise TypeError("size must be >= 0")
        elif not isinstance(size, int): 
            raise ValueError("size must be an integer")
        else:
            self._Square__size = size
