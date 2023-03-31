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
        return self.width

    @size.setter
    def size(self, width):
        """ setting width """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = width
            self.height = width

    def __update(self, id=None, size=None, x=None, y=None):
        """ assigns an argument to each attribute """
        if id is not None:
            self.id = id
        if size is not None:
            self.width = size
            self.height = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
