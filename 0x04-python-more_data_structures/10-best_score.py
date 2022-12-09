#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = max(a_dictionary.values(), default=None)
    for key in a_dictionary.keys():
        if best == a_dictionary[key]:
            return key
    return None
