#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    holder = []
    result = None
    for i in args:
        holder.append(i)
    try:
        result = fct(*holder)
    except Exception as e:
        print("Exception: {}".format(e), file = sys.stderr)
    return result
