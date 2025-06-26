#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[]]
    for index_1, row in enumerate(matrix):
        for index_2, col in enumerate(row):
            new_matrix[index_1][index_2].append(col**2)
    return new_matrix
