#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        """prints x element of a list

        Args:
            my_list: input list
            x = numbers of element to print

        Returns:
            The number of elements printed
        """
        tmp = 0
        for i in range(x):
            try:
                print(f"{my_list[i]}", end='')
                tmp += 1
            except IndexError:
                break
        print()
        return tmp
