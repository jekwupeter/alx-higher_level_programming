#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    new_in_list - modifies list without changing original
    @idx: index of replacement element
    @element: repalcement element
    """
    list_copy = my_list[:]
    if idx < 0:
        return list_copy
    elif idx >= len(my_list):
        return list_copy
    else:
        for id, item in enumerate(list_copy):
            if idx == id:
                list_copy[id] = element
                return list_copy
