#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers

    Args:
        my_list: input list
        x = number of element to access in list

    Return:
        real number of integers printed
    """
    tmp = 0
    for i in range(x):
        try:
            buff = int(my_list[i])
            print("{:d}".format(buff), end='')
            tmp += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print("")
    return tmp
