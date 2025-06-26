#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        max = None
        return max
    max = my_list[0]
    i = 0
    while (i + 1) < len(my_list):
        if max < my_list[i + 1]:
            max = my_list[i + 1]
        else:
            pass
        i += 1
    return max
