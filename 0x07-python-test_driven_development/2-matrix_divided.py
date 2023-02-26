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
    if (type(matrix) is not list or (len(matrix) == 0) or
       type(matrix[0]) is not list or (len(matrix[0]) == 0)):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if num is None or (type(num) is not int and
                               type(num) is not float):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    return([[round(num / div, 2) for num in row] for row in matrix])
