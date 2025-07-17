#!/usr/bin/python3
"""This module defines a class"""


class Student:

    def __init__(self, first_name, last_name, age):
        first_name = first_name 
        last_name = last_name 
        age = age

    def to_json(self, attrs=None):
        """
        This class returns the dictionary representsation of 
        the class attributes
        """
        if isinstance(attrs, list):
            attrs_dict = {}

            for keys in attrs:
                attrs_dict[keys] = self.keys
            return attrs_dict
        return self.__dict__.copy()
