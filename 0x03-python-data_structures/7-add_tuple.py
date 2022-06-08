#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    add_tuple - adds two tuples
    @tuple_a: first input tuple
    @tuple_b: second input tuple
    """
    result = [0, 0]
    if isinstance(tuple_a, tuple):
        if len(tuple_a) != 1:
            tuple_a = list(tuple_a) if len(tuple_a) > 1 else [0, 0]
        else:
            tuple_a = [tuple_a[0], 0]
    elif isinstance(tuple_a, int) or len(tuple_a) == 1:
        tuple_a = [tuple_a, 0]
    if isinstance(tuple_b, tuple):
        if len(tuple_b) != 1:
            tuple_b = list(tuple_b) if len(tuple_b) > 1 else [0, 0]
        else:
            tuple_b = [tuple_b[0], 0]
    elif isinstance(tuple_b, int) or len(tuple_b) == 1:
        tuple_b = [tuple_b, 0]
    result[0], result[1] = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return tuple(result)
