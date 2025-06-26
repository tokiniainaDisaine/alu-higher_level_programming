#!/usr/bin/python3

def max_integer(my_list=[]):
    max = my_list[0]
    i = 0
    if not my_list:
        max = None
        return max
    while (i + 1) < len(my_list):
        if max < my_list[i + 1]:
            max = my_list[i + 1]
        else:
            pass
        i += 1
    return max
