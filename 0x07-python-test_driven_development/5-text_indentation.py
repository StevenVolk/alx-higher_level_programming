#!/usr/bin/python3

"""

A function that prints a text with 2 new lines after
each of these characters: ., ? and :

"""


def text_indentation(text):
    """

    A method that prints a text with 2 new lines
    after each of these characters: ., ? and :

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in text:
        print(char, end='')
        if char == '.' or char == '?' or char == ':':
            print()
            print()
