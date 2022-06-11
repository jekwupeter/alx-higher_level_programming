#!/usr/bin/python3
def best_score(a_dictionary):
    """
    number_keys - finds the key with biggest integer
    @a_dictionary: input dictionary
    Return: key with biggest integer
    """
    if a_dictionary == None or len(a_dictionary) == 0:
        return None

    buff = -9999
    for k, v in a_dictionary.items():
        buff = v if buff < v else buff
        return k
