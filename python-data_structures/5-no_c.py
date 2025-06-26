#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            temp_char = ''
        else:
            temp_char = i
        new_string = new_string + temp_char
    return new_string
