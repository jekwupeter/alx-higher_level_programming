#!/usr/bin/python3
"""Defines a function that prints a sqaure with a character"""
def print_square(size):
    """prints a square with the character #

    Raises:
        TypeError: if size not int
        ValueError: if size os less than zero

    Args:
        size (int): input size of square
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print('#', end="") for x in range(size)]
        print("")
