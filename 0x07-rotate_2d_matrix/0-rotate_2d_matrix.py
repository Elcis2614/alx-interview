#!/usr/bin/python3
"""
    Rotating a 2d array(list)
"""


def rotate_2d_matrix(matrix):
    """
        Rotate , does not print
    """
    length = len(matrix)
    new_m = []
    index = [x for x in range(length)]
    for i in range(length):
        mList = [matrix[k][i] for k in index]
        mList.reverse()
        new_m.append(mList.copy())
    for i in range(length):
        matrix[i] = new_m[i]
