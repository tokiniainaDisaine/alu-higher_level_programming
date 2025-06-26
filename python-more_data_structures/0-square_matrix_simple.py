#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[]]
    matrix_len = len(matrix)
    for i in range(0, matrix_len):
        matrix_1_len = len(matrix[i])
        for j in range(0, matrix_1_len):
            new_matrix[i][j].append(matrix[i][j])
    return new_matrix
