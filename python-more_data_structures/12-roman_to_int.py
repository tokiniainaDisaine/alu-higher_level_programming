#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dictionary = {
        "I" : 1,
        "II" : 2,
        "III" : 3,
        "IV" : 4,
        "V" : 5,
        "VI" : 6,
        "VII" : 7,
        "VIII" : 8,
        "IX" : 9,
        "X" : 10,
        "L" : 50, 
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    count = {
        "I" : 0,
        "II" : 0,
        "III" : 0,
        "IV" : 0,
        "V" : 0,
        "VI" : 0,
        "VII" : 0,
        "VIII" : 0,
        "IX" : 0,
        "X" : 0,
        "L" : 0, 
        "C" : 0,
        "D" : 0,
        "M" : 0
    }

    myKeys = list(roman_dictionary.keys())

    for i in myKeys:
        

    