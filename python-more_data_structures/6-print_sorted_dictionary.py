#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    myKeys = list(a_dictionary.keys())
    myKeys.sort()

    for i in myKeys:
        print("{}: {}".format(i, a_dictionary[i]))
