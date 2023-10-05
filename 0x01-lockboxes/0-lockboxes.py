#!/usr/bin/python3
"""
    method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
        Each box is numbered sequentially from 0 to n - 1 and
        each box may contain keys to the other boxes.
        returns true i fall boxes can be opened, else return False
        The first box boxes[0] is unlocked
    """
    gates = [0 for box in boxes]
    gates[0] = 1

    def openLock(addresses):
        """ Given the keys(address) the function recursively
            open boxes and updates the gates variables """
        if (addresses == []):
            return
        for address in addresses:
            if address >= len(boxes) continue
            elif gates[address] != 1:
                gates[address] = 1
                openLock(boxes[address])
                continue
            else:
                continue
    openLock(boxes[0])
    return (0 not in gates)
