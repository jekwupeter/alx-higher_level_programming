#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    boolean = False
    try:
        print("{:d}".format(value))
        boolean = True
    except Exception as e:
        print("Exception: ", e, file = sys.stderr)
