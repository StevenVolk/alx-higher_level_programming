#!/usr/bin/python3
"""

from models.base import Base

"""


from models.base import Base

"""

class Rectangle that inherits from Base

"""


class Rectangle(Base):
    """

    class Rectangle that inherits from Base

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """

        getting width

        """
        return self.__width

    @width.setter
    def width(self, width):
        """

        setting width

        """
        self.__width = width

    @height.setter
    def height(self, height):
        """

        setting height

        """
        self.__height = height

    @property
    def height(self):
        """

        getting height

        """
        return self.__height

    @property
    def x(self):
        """

        getting x

        """
        return self.__x

    @x.setter
    def x(self, x):
        """

        setting x

        """
        self.__x = x

    @property
    def y(self):
        """
        getting y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """setting y"""
        self.__y = y
