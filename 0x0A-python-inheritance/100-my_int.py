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

    def __eq__(self, other):
        """

        == operator inverted for !=

        """

        return self.integer != other

    def __ne__(self, other):
        """

        != operator inverted for ==

        """

        return self.integer == other
