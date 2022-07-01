#!/usr/bin/python3
"""Module defines an empty rectangle class"""
class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instatiation of attibutes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter property"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """sets the width propety"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter property"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """sets the height propety"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns printable format of rectangle"""
        return ("\n".join(["".join(['#' for i in range(self.__width)]) for j in range(self.__height)]))
    
    def __repr__(self):
        """returns string representation of rectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

