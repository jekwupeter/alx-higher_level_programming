def print_reversed_list_integer(my_list=[]):
    """
    print_reversed_list_integer - reverse prints list elements
    my_list: input list
    """
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(list[i]))