#!/usr/bin/python3
"""
This module adds all arguments to a Python list,
 and then save them to a file
"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item():
    """
    This function adds all arguments to a Python list,
    and then save them to a file
    """

    try:
        args = load_from_json_file("add_item.json")
    except Exception:
        args = []
    args += sys.argv[1:]

    save_to_json_file(args, "add_item.json")


add_item()
