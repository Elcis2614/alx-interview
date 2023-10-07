#!/usr/bin/python3
"""
    method that determines if all the boxes can be opened
    implemented with a simple for loop
"""


def canUnlockAll(boxes):
    """
        Each box is numbered sequentially from 0 to n - 1 and
        each box may contain keys to the other boxes.
        returns true if all boxes can be opened, else return False
        The first box boxes[0] is unlocked
    """
    opened = [0]

    def same():
        """
           Check if the two boxes are of the same length
        """
        return len(boxes) == len(opened)

    i = 0
    while i < len(opened) and not same():
        for box in boxes[i]:
            if box not in opened:
                opened.append(box)
        i += 1
    return same()
