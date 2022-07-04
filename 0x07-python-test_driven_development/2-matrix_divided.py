#!/usr/bin/python3
"""defines a function that divides a matrix by a div"""
def matrix_divided(matrix, div):
    """divides a matrix by a divider

    Args:
        matrix (int or float):
        div (int or float):

    Raises:
        TypeError: if input matrix or div is not float or int
        TypeError: if input matrix rows are not same size
        ZeroDivisionError: if div is zero

    Returns:
        a new matrix
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if len(matrix) < 2:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for li in matrix:
        if not isinstance(li, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for element in li:
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for li in matrix:
        if len(li) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    
    result = []

    for li in matrix:
        result.append([round((x / div), 2) for x in li])
    return (result)
