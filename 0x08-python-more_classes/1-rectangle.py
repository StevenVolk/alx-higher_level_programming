#!/usr/bin/python3
"""

A rectangle class

"""


class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """

        returns the value of width

        """

        return self.__width

    @width.setter
    def width(self, value):
        """

        assigns a value to width

        """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """

        returns the value of height

        """

        return self.__height

    @height.setter
    def height(self, value):
        """

        assigns a value to height

        """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
