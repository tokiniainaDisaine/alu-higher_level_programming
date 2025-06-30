#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):
        try:
            print("{:d}".format(i), end="")
        except IndexError:
            continue
    print('')
