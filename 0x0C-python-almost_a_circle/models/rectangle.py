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

    @setter
    def set_width(self, width):
        self.__width = width

    @getter
    def get_width(self):
        return self.__width

    @setter
    def set_height(self, height):
        self.__height = height

    @getter
    def get_height(self):
        return self.__height

    @setter
    def set_x(self, x):
        self.__x = x

    @getter
    def get_x(self):
        return self.__x

    @setter
    def set_y(self, y):
        self.__y = y

    @getter
    def get_y(self):
        return self.__y
