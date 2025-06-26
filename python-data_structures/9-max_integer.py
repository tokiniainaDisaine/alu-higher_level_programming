#!/usr/bin/python3

def max_integer(my_list=[]):
    max = my_list[0]
    for i in range(0, len(my_list)):
        if my_list[i] < my_list[i + 1]:
            max = my_list[i + 1]
        else:
            pass
        
    if not my_list:
        max = None

    return max
