#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)

    if (n-1) == 1:
        argument = 'argument:'
    elif (n-1) == 0:
        argument = 'arguments.'
    else:
        argument = 'arguments:'

    print(f"{n-1} {argument}")
    for i in range(1, n):
        print(f"{i}: {argv[i]}")
