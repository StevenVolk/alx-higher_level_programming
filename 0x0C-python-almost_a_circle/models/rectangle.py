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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """

        getting height

        """
        return self.__height

    @height.setter
    def height(self, height):
        """

        setting height

        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

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
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
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
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """ calculating area """
        return self.width * self.height

    def display(self):
        """ displaying rectangle with # """

        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for z in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """ Returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """

        return "[Rectangle] ({0}) {1}/{2} - {3}/{4}"\
            .format(self.id, self.__x, self.__y, self.__width, self.height)

    def update(self, *args):
        """ assigns an argument to each attribute """
        l_args = 0
        arg_data = []
        for arg in args:
            l_args += 1
            arg_data.append(arg)
        if l_args >= 1:
            self.__id(arg_data[0])
        if l_args >= 2:
            self.width(arg_data[1])
        if l_args >= 3:
            self.height(arg_data[2])
        if l_args >= 4:
            self.x(arg_data[3])
        if l_args >= 5:
            self.y(arg_data[4])
