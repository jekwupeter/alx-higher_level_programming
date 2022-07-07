#!/usr/bin/python3
"""Module define an empty class"""
class Rectangle(BaseGeometry):
    """defines a rectangle class that inheirts from another class"""
    def __init__(self, width, height):
        """initialization of instance attributes"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
