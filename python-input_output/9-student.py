#!/usr/bin/python3
"""This module defines a class"""


class Student:

    def __init__(self, first_name, last_name, age):
        first_name = first_name 
        last_name = last_name 
        age = age


    def to_json(self):
        """
        This class returns the dictionary representsation of 
        the class attributes
        """
        # final_json = {}

        # for name, value in self.__dict__.items():
        #     final_json[name] = value

        # return final_json
        return vars(self)
