#!/usr/bin/python3
"""Define an integer addition function"""

def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int): input integer
        b (int): input integer

    Raises:
        TypeError: if a or b is not int or float

    Returns:
        sum of two integers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isintance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
