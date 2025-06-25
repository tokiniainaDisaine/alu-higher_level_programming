#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(c) >= 97 and ord(c) <= 122:
            is_char = True
        else:
            is_char = False

        if is_char:
            print("{}".format(chr(char)), end="")
        else:
            print(f"{char}", end="")   
