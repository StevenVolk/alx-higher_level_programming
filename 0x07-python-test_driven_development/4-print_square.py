#!/usr/bin/python3

"""

A function that prints a square with the character #

"""


def print_square(size):
    """

    A method that prints a square with the character #

    """

    if (type(size) is float and size < 0) or type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            if j < size - 1:
                print("#", end="")
            else:
                print("#")
