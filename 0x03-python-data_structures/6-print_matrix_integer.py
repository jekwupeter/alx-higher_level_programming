#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    print_matrix_integer - prints a matrix of integers
    @matrix: input matrix
    """
    for inner_list in matrix:
        for i, element in enumerate(inner_list):
            print("{:d}".format(element), end="")
            if i != (len(inner_list) - 1):
                print(" ", end="")
        print("")
