#!/usr/bin/python3
import sys

sum = 0
for i in range(len(sys.argv)):
    sum += int(sys.argv[i])
    print("{:d}".format(sum))
