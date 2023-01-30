#!/usr/bin/python3
"""

A rectangle class

"""


class Rectangle:
    """

    initializes Rectangle class

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        global number_of_instances
        type(self).number_of_instances += 1
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

    def area(self):
        """

        returns the area of rectangle

        """

        return self.__width * self.__height

    def perimeter(self):
        """

        returns the perimeter of rectangle

        """

        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """

        print the rectangle with the character #

        """

        rect = ""
        global print_symbol
        if (self.__width == 0 or self.__height == 0):
            return rect
        for i in range(self.__height):
            for j in range(self.__width):
                rect += type(self).print_symbol
            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """

        string representation of the rectangle

        """

        return("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """

        Delete an instance of a rectangle

        """

        global number_of_instances
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
