#!/usr/bin/python3
from sys import argv
n = len(argv)
print(f"{n} arguments:")
for i in range(1, n):
    print(f"{i} {argv[i]}")