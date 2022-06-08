#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    uniq_add - adds all unique elements in a list
    @my_list: Input list
    """
    my_list_set = set(my_list)
    return (sum(my_list_set))
