#!/usr/bin/python3
"""Defines a function that prints a text with custom instruction"""
def text_indentation(text):
    """prints a text with 2 lines after each of these char['.', '?',':']
    Raises:
        TypeError: if text is not string

    Args:
        text (str): input text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special = ['.', '?',':']
    for ch in text:
        if ch not in special:
            print(ch,end='')
        else:
            print(ch,end="\n\n")
