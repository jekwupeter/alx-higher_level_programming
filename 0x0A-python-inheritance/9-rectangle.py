#!/usr/bin/python3
"""Module define an empty class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """defines a rectangle class that inheirts from another class"""
    def __init__(self, width, height):
        """initialization of instance attributes"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
    
    def area(self):
        """returns area of rectangle class instance"""
        return self.__width * self.__height

    def __str__(self):
        """Defines string representation of class"""
        return "".join(f"[Rectangle] {self.__width}/{self.__height}")
