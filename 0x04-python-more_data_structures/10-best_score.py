#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    best = None
    for key, value in a_dictionary:
        if best == None:
            best = key
        if a_dictionary[key] > a_dictionary[best]:
            best = key
    return (best)
