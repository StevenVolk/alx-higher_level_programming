#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    j = x
    for i in range(x):
        try:
            print(my_list[i], end="")
        except:
            j = i
    return(j)
