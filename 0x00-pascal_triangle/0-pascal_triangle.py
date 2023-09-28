#!/usr/bin/python3
"""
This script contains only one function which ,
construct a pascal triangle
"""


def pascal_triangle(n):
    """ return a 2D list where each each element
        is a row that contains a list of elements
        which represent the column
    """

    from math import comb
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(comb(i, j))
            triangle.append(row)
    return triangle
