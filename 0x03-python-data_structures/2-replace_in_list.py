#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    replace_in_list - repalces n element of a list at an index
    @idx: index of element to replace
    @element: replacement element
    """
    if idx < 0:
        return my_list

    elif idx > len(my_list):
        return my_list

    else:
        for id, item in enumerate(my_list):
            if id == idx:
                my_list[id] = element
        return my_list
