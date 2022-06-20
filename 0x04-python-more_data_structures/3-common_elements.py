#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    common_elements - set_1 intersect set_2
    @set_1: first input set
    @set_2: second input set
    Return: set_1 INTERSECT set_2
    """
    intersect_set = {x for x in set_1 if x in set_2}
    return intersect_set
