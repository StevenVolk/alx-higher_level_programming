#!/usr/bin/python3

"""

A class MyList that inherits from list

"""


class MyList(list):
    """

    A class MyList that inherits from list

    """

    def __init__(self):
        """

        initializing the class

        """

        super(list, self).__init__()

    def print_sorted(self):
        """

        This method prints the list, but sorted (ascending sort)

        """

        print(sorted(self))
