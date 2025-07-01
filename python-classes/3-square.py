#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
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

    def area(self):
        return self._size**2
