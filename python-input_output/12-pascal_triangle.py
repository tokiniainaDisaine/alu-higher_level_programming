#!/usr/bin/python3
"""This module implements the Pascal's triangle"""


def pascal_triangle(n):
    """This module implements the Pascal's triangle"""
    final_list = []

    if n == 0:
        return final_list
    
    for i in range(n):
        inside_list = []

        for j in range(i):
            if j == 0:
                inside_list.append(1)
            if j == i:
                inside_list.append(1)
            else:
                number = inside_list[j] + inside_list[j-1]
                inside_list.append(number)

        final_list.append(inside_list)
    
    return final_list

if __name__ == "__main__":
    triangle = pascal_triangle(5)

    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))