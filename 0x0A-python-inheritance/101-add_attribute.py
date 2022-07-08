#!/usr/bin/python3
"""Module define a function that tires to add attribute to a class"""
def add_attribute(cls, attr, attr_value):
    """defines a fucntion that tries to add new attribute to a clas

    Args:
        cls (class): input class
        attr: attribute of class
        attr_value: new attribute value of class

    Raises:

    """
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(cls, attr, attr_value)
