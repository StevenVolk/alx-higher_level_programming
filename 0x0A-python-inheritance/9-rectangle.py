#!/usr/bin/python3
"""

A class BaseGeometry (based on 7-base_geometry.py).
task based on 8-rectangle.py

"""


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

        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """

        Calculates the area of rectangle (height * width)

        """

        return (self.__height * self.__width)

    def __str__(self):
        """

        returns rectangle description: [Rectangle] <width>/<height>

        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
