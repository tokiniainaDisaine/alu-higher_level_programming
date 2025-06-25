#!/usr/bin/python3
def uppercase(str):
    for char in str:
        is_char = False
        if ord(char) >= 97 and ord(char) <= 122:
            is_char = True
        else:
            continue

        if is_char:
            print("{}".format(chr(char)), end="")
        else:
            print(f"{char}", end="")  
