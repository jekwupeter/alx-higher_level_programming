#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    arg_list = []
    if len(sys.argv) == 1:
        print("{:d}".format(sum))
    else:
        for i in range(len(sys.argv)):
            if i != len(sys.argv):
                arg_list.append(int(sys.argv[i + 1]))
                print(arg_list)
                print(f"{sum(arg_list)}")
