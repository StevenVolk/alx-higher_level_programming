#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda inner_list : list(map(lambda i : i * i, inner_list)), matrix))
