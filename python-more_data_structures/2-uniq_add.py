#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = list(set(my_list))
    total = 0

    for i in unique_elements:
        total = total + int(i)

    print("Total: {:d}".format(total))
