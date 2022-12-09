#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_dictionary = sorted(a_dictionary.items(), key = lambda kv: kv[0])
    for key, value in s_dictionary:
        print("{0}: {1}".format(key, value))
