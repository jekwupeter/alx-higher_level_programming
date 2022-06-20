#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with f-string format

    Args:
        value: input data of any type

    Return:
        True if correct logical execution else false
    """
    checker = False
    try:
        buffer = int(value)
        print("{:d}".format(buffer))
        checker = True
    except Exception:
        pass
    return checker
