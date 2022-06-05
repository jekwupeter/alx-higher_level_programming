#!/usr/bin/python3
def no_c(my_string):
    """
    no_c - removes all characters c and C from string
    @my_string: input string
    """
    copy_str = [char for char in my_string if char != 'c' and char != 'C']
    return ("".join(copy_str))
