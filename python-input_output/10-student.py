#!/usr/bin/python3
"""This module defines a class"""


class Student:

    def __init__(self, first_name, last_name, age):
        first_name = first_name 
        last_name = last_name 
        age = age

    def to_json(self, attrs=None):
        """
        This method returns a json
        """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
            return d_list

        return obj
