#!/usr/bin/python3
"""

importing rectangle

"""


from models.rectangle import Rectangle

"""

class Square that inherits from Rectangle

"""


Square(rectangle):
    """

    class Square

    """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializing """
        super().__init__(id, size, size, x, y)

    def __str__():
        """ return [Square] (<id>) <x>/<y> - <size> """

        return "[Square] ({0}) {1}/{2} - {3}"\
            .format(self.id, self.__x, self.__y, self.__width)
