#!/usr/bin/python3
"""Module define a square class"""
class Square(Rectangle):
    """defines a rectangle class that inheirts from subclass of another class"""
    def __init__(self, size):
        """initialization of instance attributes"""
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        """finds the area of square class instance"""
        return (self.__size ** 2)
