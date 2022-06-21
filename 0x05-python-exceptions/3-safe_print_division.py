#!/usr/bin/python3
def safe_print_division(a, b):
    """divides 2 integer and print result

    Args:
        a: first integer
        b: second integer

    Return:
        value of division else "None"
    """
    result = None
    try:
        result = a/b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
