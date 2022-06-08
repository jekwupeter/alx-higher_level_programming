#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    add_tuple - adds two tuples
    @tuple_a: first input tuple
    @tuple_b: second input tuple
    """
    result = [0, 0]
    for i in range(2):
        if isinstance(tuple_a, tuple):
            tuple_a = list(tuple_a) if len(tuple_a) > 1 else [0, 0]
        elif isinstance(tuple_a, int) or len(tuple_a) == 1:
            tuple_a = [tuple_a, 0]
            break
        if isinstance(tuple_b, tuple):
            tuple_b = list(tuple_b) if len(tuple_b) > 1 else [0, 0]
        elif isinstance(tuple_b, int) or len(tuple_b) == 1:
            tuple_b = [tuple_b, 0]
            break
        result[i] = tuple_a[i] + tuple_b[i]
    return tuple(result)
