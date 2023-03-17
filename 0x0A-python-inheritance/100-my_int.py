#!/usr/bin/python3

"""

A class MyInt that inherits from int

"""


class MyInt(int):
    """

    A class MyInt that inherits from int

    """

    def __init__(self, integer):
        """

        Initializing integer

        """

        self.integer = integer

    def __eq__(self.integer, other):
        """

        == operator inverted for !=

        """

        int.__ne__(self.integer, other)

    def __ne__(self.integer, other):
        """

        != operator inverted for ==

        """

        int.__eq__(self.integer, other)
