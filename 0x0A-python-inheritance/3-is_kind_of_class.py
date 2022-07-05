#!/usr/bin/python3
"""Module defines a functions that compares class instances"""
def is_kind_of_class(obj, a_class):
    """checks if object is an instance of a class of\
            or if the object is an instance of a class\
            inherited from, the specified class
    Args:
        obj: input obj
        a_class: input class

    Returns:
        True if is instance
        False if not instance
    """
    if isinstance(obj, a_class):
        return True
    return False
