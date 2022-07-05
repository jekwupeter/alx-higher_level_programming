#!/usr/bin/python3
"""Module defines a class that inherits from list class"""
class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints a list after sorting it"""
        print(sorted(self))
