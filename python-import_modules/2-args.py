#!/usr/bin/python3
import sys
n = len(sys.argv)
print(f"{n} arguments:")
for i in range(1, n):
    print(f"{i} {sys.argv[i]}")