#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    myKeys = list(a_dictionary.keys())
    for i in myKeys:
        new_dictionary[i] = new_dictionary[i] * 2
    return new_dictionary