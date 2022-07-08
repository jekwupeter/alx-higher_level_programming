#!/usr/bin/python3
"""Module define a class that inherits from int"""
class MyInt(int):
    """defines a class that invertsw the comparison operator of int"""
    def __eq__(self, other):
        """Defines a functions that inverts equality operation"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Defines a fcuntion that invrts not equal operator"""
        return super().__eq__(other)
