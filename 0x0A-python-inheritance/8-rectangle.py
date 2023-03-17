#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
bg = BaseGeometry()

"""

A class Rectangle that inherits from BaseGeometry (7-base_geometry.py)

"""


class Rectangle(bg):
    """

    A class Rectangle that inherits from BaseGeometry

    """

    def __init__(self, width, height):
        """

        Inializing class

        """

        if bg.integer_validator(self, "width", width):
            self.width = width
        if bg.integer_validator(self, "height", height):
            self.height = height
