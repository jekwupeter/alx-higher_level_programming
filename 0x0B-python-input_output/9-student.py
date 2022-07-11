#!/usr/bin/python3
"""MOdule that defines a Student class"""
class Student:
    """"defines a Student class"""
    def __init__(self, first_name, last_name, age):
        """initialization of class instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representaion of Student instance"""
        return self.__dict__
