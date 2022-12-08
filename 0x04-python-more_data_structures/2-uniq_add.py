#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_item = set()
    add = 0
    for item in my_list:
        if item not in uniq_item:
            add += item
        else:
            uniq_item.add(item)
    return (add)
