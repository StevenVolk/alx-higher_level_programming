#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print(my_list[i], end="")
        except:
            return("\n{:d}".format(i))
    return("\n{:d}".format(x))
