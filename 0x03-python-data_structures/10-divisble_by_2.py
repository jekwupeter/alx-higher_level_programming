#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    divisible_by_2 - checks if elements in a list are divisible by two
    @my_list: Input list
    Return: New bool list
    """
    holder = []
    for element in my_list:
        if isinstance(element, int):
            holder.append(True if element % 2 == 0 else False)
        else:
            holder.append(element)
    return holder
