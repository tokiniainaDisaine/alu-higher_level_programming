#!/usr/bin/python3
"""This is a square class that does nothing"""


class Square:
    """This is a square class that stores properties of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initiator function"""

        self._size = size
        self._position = position
            
    def area(self):
        """This function returns the area of the square"""

        return self._size**2
    
    def my_print(self):
        """This function print a square using # as blocks in a 2D plane"""

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
        """This function returns the value of size"""

        return self._size

    @size.setter
    def size(self, value):
        """This function allows you to change the value of size"""

        try:
            if isinstance(value, int) and value > 0:
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
        """This function returns the value of position"""

        return self._position

    @position.setter
    def position(self, value):
        """This function allows you to change the value of position"""

        if isinstance(value, tuple) and len(value) == 2:
            self._position = value     
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
