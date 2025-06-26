#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    element_0_0 = tuple_a[0]
    element_0_1 = tuple_a[1]
    element_1_0 = tuple_b[0]
    element_1_1 = tuple_b[1]

    if len(tuple_a) < 2:
        element_0_1 = 0

    if len(tuple_b) < 2:
        element_1_1 = 0
    
    first_element = element_0_0 + element_1_0
    second_element = element_0_1 + element_1_1

    new_tuple = (first_element, second_element)
    return new_tuple
