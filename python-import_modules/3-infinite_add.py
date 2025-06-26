#!/usr/bin/python3
import sys
n = len(sys.argv)
result = 0
for i in range(1, n):
    number = int(sys.argv[i])
    result = result + number
print(result)
