#!/usr/bin/python3
"""Module defines a function that reads a text file and prints it"""
def read_file(filename=""):
    """reads a text file and prints it to stdout

    Args:
        filename: input file
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read(), end="")
