#!/usr/bin/python3
"""

models/base.py

"""


class Base:
    """

    class

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """

        init

        """

        if id != None:
            self.id = id
        else:
            __nb_objects++
            self.id = __nb_objects
