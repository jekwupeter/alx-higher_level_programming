#!/usr/bin/python3
"""Defines the sqaure class"""
class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of square class
        Args:
            size (int): size of new sqaure
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 and all(isinstance(i, int) for i in value) and all(i >= 0 for i in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        

    def area(self):
        """finds the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """prits the size of square with # chari"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            [print(" ", end="") for m in range(self.__position[0])]
            if self.__position[1] == 0:
                [print(" ", end="") for m in range(self.__position[1])]
            [print("#", end="") for j in range(self.__size)]
            print("")
