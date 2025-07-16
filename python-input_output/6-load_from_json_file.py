#!/usr/bin/python3
"""A function that creates an Object from a “JSON file”"""


import json

def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”"""

    with open(filename):
        return json.loads(filename)