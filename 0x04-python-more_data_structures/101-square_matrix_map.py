#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda inner: list(map(lambda i: i * i, inner)), matrix))
