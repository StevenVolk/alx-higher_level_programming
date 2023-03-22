#!/usr/bin/python3
"""

A function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal’s triangle of n

"""


def pascal_triangle(n):
    """

    A function def pascal_triangle(n): that returns a list of lists of integers
    representing the Pascal’s triangle of n

    """

    l_of_list = []

    if n <= 0:
        return l_of_list

    for i in range(1, n+1):
        l = []
        for j in i:
            if j == 0:
                l.append(1)
            elif j == i - 1:
                l.append(1)
            else:
                l.append(prev[j] + prev[j-1])
        l_of_list.append(l)
        prev = l

    return l_of_list
