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
    p_char = ''
    for char in text:
        if (p_char == '.' or p_char == '?' or p_char == ":") and char == ' ':
            char = ''
        if char == '.' or char == '?' or char == ':':
            print(char)
            print()
        else:
            print(char, end='')
        p_char = char
