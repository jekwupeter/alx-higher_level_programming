#!/usr/bin/python3
def safe_print_integer_err(value):
    """prints an integer

    Args:
        value: input value of any type

    Returns:
        True of value is inputed correctly else false
    """
    import sys
    boolean = False
    try:
        print("{:d}".format(value))
        boolean = True
    except(ValueError, TypeError) as e:
        print("Exception: {}".format(e), file = sys.stderr)
    return boolean
