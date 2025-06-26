#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) < 1:
        return None

    myKeys = list(a_dictionary.keys())
    max = a_dictionary[myKeys[0]]
    max_key = myKeys[0]

    for i in myKeys:
        if a_dictionary[i] > max:
            max_key = i
    return max_key
