#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    multiply_by_2 - multiples all values in a dict by two
    @a_dictionary: input dictionary
    Return: new dict with values multiplied by two
    """
    a_dictionary = {key: value * 2 for key, value in a_dictionary.items()}
    return a_dictionary
