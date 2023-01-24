#!/usr/bin/python3
"""

A class Square

"""


class Square:
    """

    A class Square

    """

    def __init__(self, size=0):
        self.size = size

    def area(self):
        try:
            return(self.__size ** 2)
        else:
            return self.size * self.size

    def size(self):
        return(self.__size)

    def size(self, value):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
