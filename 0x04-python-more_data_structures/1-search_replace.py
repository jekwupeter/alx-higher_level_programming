#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    search_replace - replaces all occurence of\
    element in a list
    @my_list: initial list
    @search: element to replace in list
    @replace: the new element
    """
    my_list = [replace if element == search else\
               element for element in my_list]
    return my_list
