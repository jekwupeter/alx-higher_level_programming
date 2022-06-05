#!/usr/bin/python3
def element_at(my_list, idx):
    """
    element_at - retrieves an element from a list using index
    @my_list: input list
    @idx: index of element to retrieve
    """
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        for id, item in enumerate(my_list):
            if id == idx:
                return item
