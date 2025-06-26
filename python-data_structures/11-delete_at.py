#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new_list = []
    j = 0
    for i in range(0, len(my_list)):
        if i == idx: 
            continue
        else:
            new_list[j] = my_list[i]
            j += 1
    my_list = new_list.copy()
    return my_list
        