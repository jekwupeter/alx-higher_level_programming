#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j and i + j != 17:
            print(f"{i:d}{j:d}", end=", ")
print(f"{i - 1}{j}")
