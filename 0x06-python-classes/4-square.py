#!/usr/bin/python3
""""Defuines the class square"""
class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Initialization of square class

        Args:
            size (int): size of new sqaure
        """
        self.size = size
    @property
    def size(self):
        """getter method to get size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method to set size of square

        Args:
            value (int): variable to hold set size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """finds the area of square"""
        return (self.__size ** 2)
