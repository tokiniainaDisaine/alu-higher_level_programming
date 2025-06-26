#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    element = [[]]
    element[0][0] = tuple_a[0] if len(tuple_a) > 1 else 0
    element[0][1] = tuple_a[1] if len(tuple_a) > 2 else 0
    element[1][0] = tuple_b[0] if len(tuple_b) > 1 else 0
    element[1][1] = tuple_b[1] if len(tuple_b) > 2 else 0
    first_element = element[0][0] + element[1][0]
    second_element = element[0][1] +  element[1][1]
    new_tuple = (first_element, second_element)
    return new_tuple
