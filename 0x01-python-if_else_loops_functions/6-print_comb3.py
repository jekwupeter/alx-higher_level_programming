#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j and i + j != 17:
            print("{:d}{:d}".format(i, j), end=", ")
print("{:d}{:d}".format(i - 1, j))
