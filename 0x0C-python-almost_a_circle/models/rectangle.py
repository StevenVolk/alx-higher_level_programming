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
    def set_width(self, width):
        """

        setting width

        """
        self.__width = width

    @width.getter
    def get_width(self):
        """

        getting width

        """
        return self.__width

    @property
    def set_height(self, height):
        """

        setting height

        """
        self.__height = height

    @height.getter
    def get_height(self):
        """

        getting height

        """
        return self.__height

    @property
    def set_x(self, x):
        """

        setting x

        """
        self.__x = x

    @x.getter
    def get_x(self):
        """
        
        getting x

        """
        return self.__x

    @property
    def set_y(self, y):
        """setting y"""
        self.__y = y

    @y.getter
    def get_y(self):
        """
        getting y
        """
        return self.__y
