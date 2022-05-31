#!/usr/bin/python3
def islower(c):
    """
    islower - checks for lower case letters
    @c: input character
    Return: True if lowercase and False if otherwise
    """
    if ord(c) in range(97, 123):
        return (True)
    else:
        return (False)
