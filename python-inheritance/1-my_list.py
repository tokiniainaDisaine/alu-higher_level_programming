#!/usr/bin/python3
"""
This module show the inheritance process in python
"""


class MyList(list):
    """This class is inherited from the list class"""

    def print_sorted(self):
        copy_list = self.copy()
        copy_list.sort()
        print(copy_list)