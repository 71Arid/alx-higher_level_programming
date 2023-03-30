#!/usr/bin/python3
""" singly linked list"""


class Node:
    """ define node class"""

    def __init__(self, data, next_node=None):
        """ Initializes node"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ retrieves data attr"""

        return self.__data

    @data.setter
    def data(self, value):
        """ sets attr """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ retrives next node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ sets next node"""

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """ linked list node"""

    def __init__(self):
        """ initializes list"""
        self.head = None

    def __str__(self):
        """ makes list printable """

        printl = ""
        location = self.head
        while location:
            printl += str(location.data) + "\n"
            location = location.next_node
        return printl[:-1]

    def sorted_insert(self, value):
        """ sorts the list"""

        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
