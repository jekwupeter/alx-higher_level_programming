#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists

    Args:
        my_list1: first input list
        my_list2: second input list
        list_length: length of output list

    Return:
        a new list with lenght = @list_length
    """
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except ValueError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
