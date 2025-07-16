#!/usr/bin/python3
"""
This module adds all arguments to a Python list,
 and then save them to a file:
"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

def add_item():
    """
    This function adds all arguments to a Python list,
    and then save them to a file:
    """
    for arg in sys.argv:
        arg = load_from_json_file(arg)
        save_to_json_file(arg, "add_item.json")