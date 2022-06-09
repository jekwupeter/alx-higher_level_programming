#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    simple_delete - delete a key/value pair using key
    @a_dictionary: input dictionary
    @key: key for item to delete
    Return: new dict with deleted key
    """
    dict_keys = [key for key in a_dictionary.keys()]
    if key in dict_keys:
        del a_dictionary[key]
    return a_dictionary
