#!/usr/bin/python3

"""

Rectangle from (9-rectangle.py)

"""


Rectangle = __import__('9-rectangle').Rectangle

"""

A class Square that inherits from Rectangle (9-rectangle.py)

"""


class Square:
    """

    A class Square that inherits from Rectangle (9-rectangle.py)

    """

    def __init__(self, size):
        """

        Initializing a class

        """

        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """

        Finds area: size * size

        """

        return self.__size * self.__size
