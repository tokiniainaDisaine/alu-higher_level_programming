#!/usr/bin/python3
"""This is a square class that does nothing"""


class Square:
    """This is a square class that stores properties of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initiator function"""

        self._size = size

        is_not_tuple = False if isinstance(position, tuple) else True
        is_not_int_0 = False if isinstance(position[0], int) else True
        is_not_int_1 = False if isinstance(position[1], int) else True

        if is_not_tuple or len(position) != 2 or is_not_int_0 or is_not_int_1:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
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
            i_min = self._position[0]
            i_max = (self._size + self._position[0])

            j_min = self._position[1]
            j_max = (self._size + self._position[1])

            if (i_min <= i <= i_max) and (j_min <= j <= j_max):
                print("")
                pass

            for i in range((self._size + self._position[0])):

                if (i_min <= i <= i_max) and (j_min <= j <= j_max):
                    print("#", end="")
                else:
                    print(" ", end="")

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

        is_not_tuple = False if isinstance(value, tuple) else True
        is_not_int_0 = False if isinstance(value[0], int) else True
        is_not_int_1 = False if isinstance(value[1], int) else True

        if is_not_tuple or len(value) != 2 or is_not_int_0 or is_not_int_1:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value
