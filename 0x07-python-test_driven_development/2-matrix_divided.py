#!/usr/bin/python3

"""

A function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """

    A method that divides all elements of a matrix.

    """

    if div is None or (type(div) is not float and type(div) is not int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    n_row = len(matrix[0])
    new_matrix = []
    for row in matrix:
        new_row = []
        if n_row != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if num is None or (type(num) is not int and
                                    type(num) is not float):
                raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
            new_num = round(num / div, 2)
            new_row.append(new_num)
        new_matrix.append(new_row)

    return(new_matrix)
