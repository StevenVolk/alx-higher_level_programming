#!/usr/bin/python3
"""

importing rectangle

"""


from models.rectangle import Rectangle

"""

class Square that inherits from Rectangle

"""


class Square(Rectangle):
    """

    class Square

    """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializing """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return [Square] (<id>) <x>/<y> - <size> """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ getting width """
        return self.__width

    @size.setter
    def size(self, width):
        """ setting width """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
            self.__height = width
