#!/usr/bin/python3
"""A function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”"""

    with open(filename, 'r', encoding="utf-8") as file:
        j_file = file.read()
        return json.loads(j_file)
