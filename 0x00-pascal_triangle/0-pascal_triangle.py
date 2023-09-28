#!/usr/bin/python3
def pascal_triangle(n):
    from math import comb

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(comb(i, j))
            triangle.append(row)
    return triangle
