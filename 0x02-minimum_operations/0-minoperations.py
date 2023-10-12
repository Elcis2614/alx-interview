#!/usr/bin/python3
"""
   Function minOperations return the number of operations
   n the number to attain
"""

from math import log


def minOperations(n):
    """
       calculates the fewest number of operations needed
       to result in exactly n H characters in the file
    """
    if (n <= 1):
        return 0
    least_power = int(log(n, 2))

    if (2 ** least_power == n):
        return least_power * 2
    else:
        least_square = 2 ** least_power
        if (n == (least_square + least_square/2)):
            return (2 * least_power) + 1
        return (2 * least_power) + 2
