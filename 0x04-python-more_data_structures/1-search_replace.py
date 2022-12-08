#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = list(my_list)
    length = len(new_list)
    for item in range(length):
        if new_list[item] == search:
            new_list[item] = replace
    return (new_list)
