#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    best = max(a_dictionary.values())
    for key, value in a_dictionary:
        if best == value:
            return (key)
