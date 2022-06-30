#!/usr/bin/python3
"""Defines a function that multiplies 2 matrices using numpy"""
import numpy as np
def lazy_matrix_mul(m_a, m_b):
    """multiplies two matrix using numpy

    Args:
        m_a (int or float): input matrix
        m_b (int or float): input matrix

    Returns:
        new matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for li in m_a:
        if not isinstance(li, list):
            raise TypeError("m_a must be a list of lists")
    for li in m_b:
        if not isinstance(li, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for li in m_a:
        for x in li:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError("m_a should contain only integers or floats")
    for li in m_b:
        for x in li:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError("m_b should contain only integers or float")
    for li in m_a:
        if len(li) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for li in m_b:
        if len(li) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_b) != len(m_a[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    return (np.matmul(m_a, m_b))
