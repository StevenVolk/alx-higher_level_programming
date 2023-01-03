#!/usr/bin/python3
"""

A rectangle class

"""


class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width(width)
        self.height(height)

    def width(self):
        """

        returns the value of width

        """

        return self.__width

    def width(self, value):
        """

        assigns a value to width

        """

        if self.check_value_int(value) is False:
            raise TypeError("width must be an integer")

        if self.check_positive(value) is False:
            raise ValueError("width must be >= 0")

        self.__width = value

    def height(self):
        """

        returns the value of height

        """

        return self.__height

    def height(self, value):
        """

        assigns a value to height

        """

        if self.check_value_int(value) is False:
            raise TypeError("height must be an integer")

        if self.check_positive(value) is False:
            raise ValueError("height must be >= 0")

        self.__height = value

    def check_value_int(self, value):
        """

        checks if a value is of type int

        """
        
        if type(value) is int:
            return True
        return False

    def check_positive(self, value):
        """

        check if a value is greater or equal to zero

        """

        if value >= 0:
            return True
        return False
