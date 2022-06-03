#!/usr/bin/python3
def remove_char_at(str, n):
    """
    remove_char_at - removes char at a specific position
    @str: input string
    @n: index positon of char to be removed
    Return: modified copy of string
    """
    if n > -1:
        str_copy = str[:n] + str[n + 1:]
    else:
        return(str)
    return (str_copy)
