#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    add_tuple - adds two tuples
    @tuple_a: first input tuple
    @tuple_b: second input tuple
    """
    result = []
    for i in range(2):
        if ![tuple_a[i]]:
            tuple_a[i] = 0
        if ![tuple_b[i]]:
            tuple_b[i] = 0
        result[i] = tuple_a[i] + tuple_b[i]
    return tuple(result)
