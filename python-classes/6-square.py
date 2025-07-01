#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self._size = size
        self._position = position
            
    def area(self):
        return self._size**2
    
    def my_print(self):
        if self._size == 0:
            print("")
            return 0

        for j in range((self._size + self._position[1])):
            for i in range((self._size + self._position[0])):
                i_limitations = (self._position[0], (self._size + self._position[0]))
                j_limitations = (self._position[1], (self._size + self._position[1]))

                if (i_limitations[0] <= i <= i_limitations[1]) and (j_limitations[0] <= j <= j_limitations[1]):
                    print("#", end="")
                else:
                    print(" ", end="")
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

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        try:
            if value.is_integer() and value > 0:
                self._position = value
            elif value < 0:
                raise ValueError
            else: 
                raise TypeError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
