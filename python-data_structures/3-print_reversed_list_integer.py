#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    length = len(my_list) + 1
    for i in range(1, length):
        print("{:d}".format(my_list[-i]))    
