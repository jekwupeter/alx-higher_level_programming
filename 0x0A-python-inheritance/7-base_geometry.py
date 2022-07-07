#!/usr/bin/python3
"""Module defines BaseGeometry class"""
class BaseGeometry():
    """defines a class"""
    def __init__(self):
        """initialization of instance attributes"""
        pass

    def area(self):
        """a public method that does nothing"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method that validates a value
        Args:
            name (str)
            value (int)
        
        Raises:
            TypeError: if value is not integer
            ValueError: if value is not greate than 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
