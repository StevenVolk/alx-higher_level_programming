#!/usr/bin/python3

"""

A class BaseGeometry (based on 6-base_geometry.py)

"""


class BaseGeometry:
    """

    A class BaseGeometry

    """

    def area(self):
        """

        A method that raises an Exception with the message area() is not
        implemented

        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """

        A method that validates value

        """

        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
