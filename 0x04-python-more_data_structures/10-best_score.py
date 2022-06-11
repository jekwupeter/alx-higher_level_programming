#!/usr/bin/python3
def best_score(a_dictionary):
    """
    number_keys - finds the key with biggest integer
    @a_dictionary: input dictionary
    Return: key with biggest integer
    """
    if a_dictionary == None or len(a_dictionary) == 0:
        return None

    buffer = -9999
    for k in a_dictionary:
        buffer = a_dictionary[k] if a_dictionary[k] > buffer else buffer
    for key in a_dictionary:
        if buffer == a_dictionary[key]:
            return key
