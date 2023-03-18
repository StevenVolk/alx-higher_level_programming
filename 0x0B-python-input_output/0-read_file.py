#!/usr/bin/python3

"""

A function that reads a text file (UTF8) and prints it to stdout

"""


def read_file(filename=""):
    """

    A function that reads a text file (UTF8) and prints it to stdout

    """

    with open(filename) as text:
        print_out = text.read()
        print(print_out)
