#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new_list = []
    j = 0
    for i in range(0, len(my_list)):
        if i == idx: 
            pass
        else:
            new_list.append(my_list[i])
    my_list = new_list.copy()
    return new_list
