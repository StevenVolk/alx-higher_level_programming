#!/usr/bin/python3
"""

A class Square

"""


class Square:
    """

    A class Square

    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    def area(self):
        return (self.size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        return (self.size == other.size)

    def __ne__(self, other):
        return (self.size != other.size)

    def __le__(self, other):
        return (self.size <= other.size)

    def __ge__(self, other):
        return (self.size >= other.size)

    def __lt__(self, other):
        return (self.size < other.size)

    def __gt__(self, other):
        return (self.size > other.size)
