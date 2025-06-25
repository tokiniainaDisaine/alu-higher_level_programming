#!/usr/bin/python3
def uppercase(str):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for char in str:
        if char.islower():
            for i in range(0, 26):
                if char == lower_alphabet[i]:
                    temp_letter = upper_alphabet[i]
        else:
            temp_letter = char
        result = result + temp_letter

# idk
