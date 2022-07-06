#!/usr/bin/python3
"""Module defines a fucntion that checks if an object is an instance of a class"""
def inherits_from(obj, a_class):
    """checks a if an object inherited from a class\
            (directly or indirectly) from the specified class

    Args:
        obj: input object
        a_class: input class

    Returns:
        True if is instance
    """
    result = False

    if isinstance(obj, a_class) and type(obj) != a_class:
        result = True
    return result
