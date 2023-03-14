#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""

A class Rectangle that inherits from BaseGeometry (7-base_geometry.py)

"""


class Rectangle(BaseGeometry):
    """

    A class Rectangle that inherits from BaseGeometry

    """

    def __init__(self, width, height):
        """

        Inializing class

        """

        if BaseGeometry.integer_validator(self, width):
            self.width = width
        if BeseGeometry.integer_validator(self, height):
            self.height = height
