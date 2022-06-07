#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    max_integer - finds biggest integer of a list.
    @my_list: Input list
    Return: max integer
    """
    if len(my_list) == 0:
        return None

    temp = -9999
    for x in my_list:
        temp = x if x > temp else temp
    return temp
