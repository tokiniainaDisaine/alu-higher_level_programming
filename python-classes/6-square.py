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

        print('\n'*self._position[1], end='')
        for i in range(self._size):
            print(' '*self._position[0], end='')
            print('#'*self._size)

    @property
    def size(self):
        """This function returns the value of size"""

        return self._size

    @size.setter
    def size(self, value):
        """This function allows you to change the value of size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    @property
    def position(self):
        """This function returns the value of position"""

        return self._position

    @position.setter
    def position(self, value):
        """This function allows you to change the value of position"""

        # is_tuple = True if isinstance(value, tuple) else False

        # if isinstance(value[0], int) or value[0] > 0:
        #     is_int_0 = True
        # else:
        #     is_int_0 = False

        # if isinstance(value[1], int) or value[1] >= 0:
        #     is_int_1 = True
        # else:
        #     is_int_1 = False

        # if not is_tuple or len(value) != 2 or not is_int_0 or not is_int_1:
        if not (isinstance(value, tuple) and len(value) == 2 and
            isinstance(value[0], int) and value[0] >= 0 and
            isinstance(value[1], int) and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self._position = value
