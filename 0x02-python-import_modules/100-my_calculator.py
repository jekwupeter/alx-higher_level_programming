#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul

    if len(sys.argv) != 4:
        print(r"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, add(a, b)))
    elif sys.argv[2] == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, sub(a, b)))
    elif sys.argv[2] == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, mul(a, b)))
    elif sys.argv[2] == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, div(a, b)))
    else:
        print(r"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
