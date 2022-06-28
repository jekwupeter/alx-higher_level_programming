#!/usr/bin/python3
""""Defines a square class"""
class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Initialization of square class

        Args:
            size (int): size of new sqaure
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """finds area of square"""
        return (self.__size ** 2)
