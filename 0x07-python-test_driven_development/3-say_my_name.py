#!/usr/bin/python3
"""Defines a fucntion that prints the user full name"""
def say_my_name(first_name, last_name=""):
    """prints first name and last name

    Raises:
        TypeError: if input not string
    Args:
        first_name (str): first name of user
        last_name (str): last name of user
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
