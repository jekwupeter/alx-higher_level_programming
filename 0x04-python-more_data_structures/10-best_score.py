#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    multiply_list - multiplies each element in iterable by number
    @my_list: input list
    @number: number to mult element in list by
    """
    mapped_list = list(map(lambda x: x * number, my_list))
    return mapped_list
