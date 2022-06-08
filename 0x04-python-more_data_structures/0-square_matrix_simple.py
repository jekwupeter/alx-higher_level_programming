#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = [[x ** 2 for x in y] for y in matrix]
    return matrix_copy
