#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    square_matrix_simple - creates a new matrix containing elements\
    raise to power two
    @matrix: input matrix
    Return: new matrix with all elements squared
    """
    matrix_copy = [[x ** 2 for x in y] for y in matrix]
    return matrix_copy
