#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    for i in my_list:
        try:
            print("{:d}".format(i), end=" " if i != my_list[-1] else '\n')
        except ValueError:
            pass
