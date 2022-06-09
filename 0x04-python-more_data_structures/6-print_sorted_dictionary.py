#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    prints_sorted_dictrionary - Prints sorted dictionary
    @a_dictionary: input dictionary
    """
    dict_keys = [key for key in a_dictionary.keys()]
    dict_keys = sorted(dict_keys)
    [print(f"{i}: {a_dictionary[i]}") for i in dict_keys]
