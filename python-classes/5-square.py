#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self._size = size
            
    def area(self):
        return self._size**2
    
    def my_print(self):
        if self._size == 0:
            print("")
            return 0

        for i in range(self._size):
            for j in range(self._size):
                print("#", end="")
            print("")
    
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        try:
            if value.is_integer() and value > 0:
                self._size = value
            elif value < 0:
                raise ValueError
            else: 
                raise TypeError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
   