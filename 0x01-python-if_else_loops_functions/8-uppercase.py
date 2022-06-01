#!/usr/bin/python3
def uppercase(str):
    """
    uppercase - prints a string in uppercase
    @str - input string
    """
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print()
