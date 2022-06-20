#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    update_dictionary - Replaces key/value pair in a dict
    @a_dictionary: input dictionary
    @key: key of replacement
    @value: value of replacement
    """
    a_dictionary[key] = value
    return a_dictionary
