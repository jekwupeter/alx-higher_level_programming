#!/usr/bin/python3
"""Defines a function that multiples 2 matrices"""
def matrix_mul(m_a, m_b):
    """multiples two matrices
    Raises:
        TypeError: if inputs are not a list or list of list
        ValueError: if input is empty list
        TypeError: if input list element is not int or float
        TypeError: if input lists rows are not of same length

    Args:
        m_a (int or float): first input matrix
        m_b (int or float): second input matrix
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
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
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
    result = []
    tmp_b = []
    for i in range(len(m_b[0])):
        new_row = []
        for j in range(len(m_b)):
            new_row.append(m_b[j][i])
        tmp_b.append(new_row)

    for r in m_a:
        new_row = []
        for c in tmp_b:
            res = 0
            for i in range(len(tmp_b[0])):
                res += r[i] * c[i]
            new_row.append(res)
        result.append(new_row)
    return (result)
