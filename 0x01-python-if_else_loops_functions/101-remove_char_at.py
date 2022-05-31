def remove_char_at(str, n):
    """
    remove_char_at - removes char at a specific position
    @str: input string
    @n: index positon of char to be removed
    Return: modified copy of string
    """
    str_copy = str[:n] + str[n + 1: ]
    return (str_copy)
