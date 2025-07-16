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
        # final_json = {}

        # for name, value in self.__dict__.items():
        #     final_json[name] = value

        # return final_json

        if isinstance(attrs, list):
            attrs_dict = {}

            for keys in attrs:
                attrs_dict[keys] = self.keys
            return attrs_dict
        return vars(self)
    

    def reload_from_json(self, json):
        del first_name
        del last_name
        del age

        for name, value in json.items():
            self.name = value

