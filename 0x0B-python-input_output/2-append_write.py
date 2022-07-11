#!/usr/bin/python3
"""Module defines fucntion that appends a string\
        at the end of the text file(UTF8)"""
def append_write(filename="", text=""):
    """appends string at the end of a text file
    
    Args:
        filename: file to be appended
        text: input text file

    Returns:
        number of characters added
    """
    with open(filename, mode="a+", encoding="utf-8") as f:
        total = f.write(text)
    return total
