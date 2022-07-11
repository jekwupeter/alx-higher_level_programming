#!/usr/bin/python3
"""Module defines a function that wrties\
        a string to a text file with UTF8 ecod"""
def write_file(filename="", text=""):
    """writes a string of text to a file

    Args:
        filename: filename of file for string to be written to
        text: text to be written to file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        total = f.write(text)
    return total
