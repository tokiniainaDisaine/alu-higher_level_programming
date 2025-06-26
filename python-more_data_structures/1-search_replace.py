#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    length = len(my_list)

    for i in range(0, length):
        if my_list[i] == search:
            new_list[i] = replace
        else:
            continue

    return new_list
