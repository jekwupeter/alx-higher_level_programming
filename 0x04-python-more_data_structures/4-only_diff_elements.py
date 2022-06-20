#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    only_diff_elements - set of all elements present in only one set.
    @set_1: first input set
    @set_2: second input set
    Return: set_1 DIFFERENCE set_2 UNION set_2 DIFFERENCE set_1
    """
    diff_set_1 = {x for x in set_1 if x not in set_2}
    diff_set_2 = {x for x in set_2 if x not in set_1}
    union_set = set.union(diff_set_1, diff_set_2)
    return union_set
