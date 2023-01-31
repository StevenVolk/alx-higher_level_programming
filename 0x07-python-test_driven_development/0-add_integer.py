#!/usr/bin/python3

"""

a function that adds 2 integers.

"""


def add_integer(a, b=98):
    """

    a method that adds 2 integers

    """

    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")

    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")

    if type(a) is float and type(b) is float:
        return(int(a) + int(b))
    elif type(a) is float:
        return(int(a) + b)
    elif type(b) is float:
        return(a + int(b))
    else:
        return(a + b)
