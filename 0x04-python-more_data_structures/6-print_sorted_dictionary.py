#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted(a_dictionary, key = a_dictionary.keys())
    for items in a_dictionary:
        print("{}: {}", items[0], items[1])
