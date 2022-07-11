#!/usr/bin/python3
"""Moduele defines a function that creates list of intger\
        representing the pascal triangle of n"""
def pascal_triangle(n):
    """creates a list representaion fo pascal traingle of a nuimber

    Args:
        n (int): input number

    Returns:
        Zero if input is less than 1
        else list of lists of integer
    """
    li = [[0 for j in range(i+1)]for i in range(n)]
    return li
