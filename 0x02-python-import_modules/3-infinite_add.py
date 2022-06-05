#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    infinite_sum = 0
    arg_list = []
    if len(sys.argv) == 1:
        print("{:d}".format(infinite_sum))
    else:
        for i in range((len(sys.argv) - 1)):
                arg_list.append(int(sys.argv[i + 1]))
        infinite_sum = sum(arg_list)
        print(f"{infinite_sum}")
