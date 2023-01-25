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
        if type(value) is not Node or value is not None:
            raise TypeError("next_node must be a Node object")
        self.next_node = value


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
        prev_node = None
        node = self.__head
        while(node):
            if new_node.data < node.data:
                if prev:
                    prev.next = new_node
                new_node.next = node
                break
            else:
                node = node.next_node

    def __str__(self):
        node = self.__head
        while(node):
            print(node.data)
            node = node.next_node
