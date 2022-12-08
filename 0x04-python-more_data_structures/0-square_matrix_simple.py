#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    rows = len(new_matrix)
    for row in range(rows):
        columns = len(row)
        for column in range(columns):
            new_matrix[row][column] = matrix[row][column] ** 2
    return (new_matrix)
