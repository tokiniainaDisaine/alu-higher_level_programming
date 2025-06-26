#!/usr/bin/python3
def best_score(a_dictionary):
    new_dictionary = a_dictionary.copy()
    myKeys = list(a_dictionary.keys())
    max = new_dictionary[myKeys[0]]

    for i in myKeys:
        if new_dictionary[i] > max:
            max = new_dictionary[i]
    return max
