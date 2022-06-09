#!/usr/bin/python3
def best_score(a_dictionary):
    """
    multiply_by_2 - checks for key with the largest value
    @a_dictionary: input dictionary
    Return: key with largest int value
    """
    if a_dictionary == None or len(a_dictionary) == 0:
        return None

    largest_value = [-9999, None]
    for k, v in a_dictionary.items():
        if int(v) > largest_value[0]:
            largest_value = [v, k]
    return largest_value[1]
