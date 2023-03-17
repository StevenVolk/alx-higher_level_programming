#!/usr/bin/python3

"""

A class MyInt that inherits from int

"""


class MyInt(int):
    """

    A class MyInt that inherits from int

    """

    def __eq__(self, other):
        """

        == operator inverted for !=

        """

        int.__ne__(self, other)

    def __ne__(self, other):
        """

        != operator inverted for ==

        """

        int.__eq__(self, other)
