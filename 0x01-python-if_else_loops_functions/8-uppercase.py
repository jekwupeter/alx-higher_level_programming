#!/usr/bin/python3
def uppercase(str):
    """
    uppercase - prints a string in uppercase
    @str - input string
    """
    print(''.join(['{:c}'.format(ord(c) - 32) if ord(c) in range(97, 123)
                  else c for c in str]))
