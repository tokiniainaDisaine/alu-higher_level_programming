#!/usr/bin/python3

def multiple_returns(sentence):
    new_tuple = (len(sentence), sentence[0])

    if sentence == '':
        new_tuple = (len(sentence), None)

    return new_tuple
