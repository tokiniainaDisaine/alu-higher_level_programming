#!/usr/bin/python3
class Square:
    """This is a square class that checks if the initial value is an integer"""

    def __init__(self, size=0):
        """This function checks if the argument is an integer"""

        try:
            if size.is_integer() and size > 0:
                self._size = size
            elif size < 0:
                raise ValueError
            else: 
                raise TypeError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
