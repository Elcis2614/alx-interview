#!/usr/bin/python3
"""
    Program to calcute the perimeter of a island (grid)
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes”
"""


COUNT = 0


def traverse(i, j, grid):
    """
        Traverses the island in a recursive manner
        i: line index
        j: column index
    """
    if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
        return 0
    elif grid[i][j] != 1:
        return grid[i][j]
    grid[i][j] = -1
    back = traverse(i, j - 1, grid)
    up = traverse(i - 1, j, grid)
    foward = traverse(i, j + 1, grid)
    down = traverse(i + 1, j, grid)
    t_count = [back, up, foward, down].count(0)
    globals()["COUNT"] += t_count
    return t_count


def island_perimeter(grid):
    """
        Entry Point,
        Grid: list of integers where :
        0 and 1 represent water and land respectively
        each cell is a square of length 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
    """
    if grid is None:
        return 0
    line_index = 0
    col_index = 0
    for i in range(len(grid)):
        if 1 in grid[i]:
            line_index = i
            col_index = grid[i].index(1)
            break
    else:
        return 0
    traverse(line_index, col_index, grid)
    return globals()["COUNT"]
