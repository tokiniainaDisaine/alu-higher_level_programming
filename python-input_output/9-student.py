#!/usr/bin/python3
"""This module defines a class"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name 
        self.last_name = last_name 
        self.age = age


    def to_json(self):
        """
        This class returns the dictionary representsation of 
        the class attributes
        """
        return self.__dict__.copy()