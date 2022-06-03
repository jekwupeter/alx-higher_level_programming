#!/usr/bin/python3
import sys

print("{:d} argument:".format(len(sys.argv)))
for i in range(len(sys.argv)):
    print("{:d}: {:s}".format(i + 1, sys.argv[i]))
