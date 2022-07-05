#!/usr/bin/python3
"""Module defines a functions that compares class instances"""
def is_same_class(obj, a_class):
    """checks if object is an instance of a class
    Args:
        obj: input obj
        a_class: input class        

    Returns:
        True if is instance
        False if not instance
    """
    if type(obj) == a_class:
        return True
    return False
