#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    complex_delete - deletes an item from dictionary
    @a_dictionary: Input dict
    @value: Value to delete
    Return: modified dict
    """
    to_delete = []
    for key in a_dictionary:
        if value == a_dictionary[key]:
            to_delete.append(key)
    for k in to_delete:
        a_dictionary.pop(k, None)
    return a_dictionary
