#!/usr/bin/python3
def uppercase(str):
    """
    uppercase - prints a string in uppercase
    @str - input string
    """
    for i in str:
        if ord(i) in range(97, 123):
            print("{:s}".format(chr(ord(i) - 32)), end="")
        else:
            print("{:s}".format(i), end="")
    print()
