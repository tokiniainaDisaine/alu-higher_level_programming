#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()

    for i in new_list:
        if i == search:
            i = replace
        else:
            continue

    return new_list
