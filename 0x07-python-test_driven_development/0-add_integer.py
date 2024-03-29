#!/usr/bin/python3

"""

a function that adds 2 integers.

"""


def add_integer(a, b=98):
    """

    a method that adds 2 integers

    """

    if a is None or (type(a) is not float and type(a) is not int):
        raise TypeError("a must be an integer")

    if b is None or (type(b) is not float and type(b) is not int):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
