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

    @dispatch(Square)
    def __str__(self):
        """ return [Square] (<id>) <x>/<y> - <size> """
        return "[{}] ({}) {}/{} - {}"\
            .format(type(self).__name__, self.__x, self.__y, self.__width)
