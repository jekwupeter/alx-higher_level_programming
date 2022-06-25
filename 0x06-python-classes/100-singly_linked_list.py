#!/usr/bin/python3
"""defines classes used in making linked list"""

class Node:
    """defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """gets the instance attribute to be made private"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """"sets the current data of the llist node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """initialiazation of instance attributes"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)
        if self.__head == None:
            #new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node != None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
    """changes the format of value to print std output"""
        value = ""
        node = self.__head
        while node is not None:
            value += str(node.data) + "\n"
            node = node.next_node
        return value[:-1]
