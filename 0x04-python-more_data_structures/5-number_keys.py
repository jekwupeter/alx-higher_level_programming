#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    number_keys - counts the number of keys in a dictionary
    @a_dictionary: input dictionary
    Return: dict key count
    """
    key_count = 0
    for i in range(len(a_dictionary.keys())):
        key_count += i
    return key_count
