#!/usr/bin/python3
"""Module defines the function that gets all the attributes and method of an object"""
def lookup(obj):
    """Returns a list of availbale attribute and method

    Args:
        obj: input object

    Returns:
        List of available method"""
    return list(dir(obj))
