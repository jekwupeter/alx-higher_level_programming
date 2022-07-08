#!/usr/bin/python3
"""Module define a function that tires to add attribute to a class"""
def add_attribute(cls, old_a, new_a):
    """defines a fucntion that tries to add new attribute to a clas
    
    Args:
        cls (class): input class
        old_attr (atrr): old attribute of class
        new_attr (attr): new attribute of class

    Raises:
        
    """
    if getattr(cls, old_a):
        raise TypeError("can't add new attribute")

    return setattr(cls, old_a, new_a)
