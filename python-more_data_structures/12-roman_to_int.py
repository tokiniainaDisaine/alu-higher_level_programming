#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {
        "I" : 1,
        # "II" : 2,
        # "III" : 3,
        # "IV" : 4,
        "V" : 5,
        # "VI" : 6,
        # "VII" : 7,
        # "VIII" : 8,
        # "IX" : 9,
        "X" : 10,
        "L" : 50, 
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        current_value = roman_values[char]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total
    