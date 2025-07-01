#!/usr/bin/python3
"""This is a square class that does nothing"""


class Square:
    """This is a square class that stores a size and can calculate the area"""

    def __init__(self, size=0):
        """This function checks if the argument is an integer"""

        try:
            if isinstance(size, int) and size > 0:
                self._size = size
            elif size < 0:
                raise ValueError
            else: 
                raise TypeError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        """This function returns the area of the square"""

        return self._size**2
