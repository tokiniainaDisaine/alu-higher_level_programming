#!/usr/bin/python3
"""
This function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    This function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
