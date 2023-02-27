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
    p_char = False
    for char in text:
        if (p_char == True) and char == ' ':
            pass
        elif char == '.' or char == '?' or char == ':':
            print(char)
            print()
            p_char = True
        else:
            print(char, end='')
            p_char = False
