#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    weight_average - calculates weighted average of list
    @my_list: input list
    Return: weighted_average
    """
    if my_list == None or len(my_list) == 0:
        return 0

    result = 0
    last_item = []
    temp_mul = 1
    # iterate through the main list
    for i in range(len(my_list)):
        my_list[i] = list(my_list[i])
        temp_mul = 1
        #iterate through the tuple inside list
        for id, item in enumerate(my_list[i]):
            temp_mul *= item
            if id == len(my_list[i]) - 1:
                last_item.append(item)
        #add the multiplication of items in inner tuple together
        result += temp_mul
    result = result/ sum(last_item)
    return result
