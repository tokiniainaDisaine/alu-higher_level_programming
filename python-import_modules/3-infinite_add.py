#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    result = 0
    for i in range(1, n):
        number = int(argv[i])
        result = result + number
    print(result)
