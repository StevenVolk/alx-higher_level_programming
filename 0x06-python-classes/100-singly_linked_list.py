#!/usr/bin/python3
"""

A node of a singly linked list

"""


class Node:
    """

    A node of a singly linked list

    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return(self.__data)

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not(value is None or type(value) is Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""

A singly linked list

"""


class SinglyLinkedList:
    """

    A singly linked list

    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        prev = None
        node = self.__head
        while(node):
            if new_node.data < node.data:
                if prev:
                    prev.next_node = new_node
                else:
                    self.__head = new_node
                new_node.next_node = node
                break
            elif node.next_node is None:
                node.next_node = new_node
                break
            else:
                prev = node
                node = node.next_node

    def __str__(self):
        node = self.__head
        d = ""
        while(node):
            d += "{:d}".format(node.data)
            node = node.next_node
            if node:
                d += "\n"
        return(d)
