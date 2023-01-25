#!/usr/bin/python3
"""

A class Square

"""


class Square:
    """

    A class Square

    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

        if len(position) != 2 or type(position[0]) is not int or \
                type(position[1]) is not int or position[0] < 0 or \
                position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = position

    def area(self):
        return(self.size ** 2)

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for k in range(self.position[1]):
                print()
            for i in range(self.size):
                for z in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value[0]) is not int or \
                type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        data = ""
        if self.size == 0:
            data += "\n"
        else:
            for k in range(self.position[1]):
                data += "\n"
            for i in range(self.size):
                for z in range(self.position[0]):
                    data += " "
                for j in range(self.size):
                    data += "#"
                if i < self.size - 1:
                    data += "\n"
        return(data)
