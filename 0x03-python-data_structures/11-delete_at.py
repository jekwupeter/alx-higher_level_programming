#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    delete_at - delete item at a specific index
    @my_list: Input index
    """
    if idx > -1 and len(my_list) > idx:
        del(my_list[idx])
    return my_list
