#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list) + 1
    if not my_list:
        return None
    for i in range(1, length):
        print("{:d}".format(my_list[-i]))    
