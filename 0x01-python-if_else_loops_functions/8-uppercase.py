#!/usr/bin/python3
def uppercase(str):
    """
    uppercase - prints a string in uppercase
    @str - input string
    """
    for i, char in enumerate(str):
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        if i != len(str) - 1:
            print("{:s}".format(char), end="")
        else:
            print("{:s}".format(char))
