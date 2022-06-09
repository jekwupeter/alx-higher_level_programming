#!/usr/bin/python3
def best_score(a_dictionary):
    """
    multiply_by_2 - checks for the largest value
    @a_dictionary: input dictionary
    Return: largest value
    """
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    largest_value = -9999
    for i in a_dictionary.values():
        if i > largest_value:
            largest_value = i
    return largest_value
