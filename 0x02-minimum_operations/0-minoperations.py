#!/usr/bin/python3
"""
   Function minOperations return the number of min. operations
   needed to result in exactly n H characters
   with only two operations possible CopyAll and Paste
   n the number to attain
"""

import math


def minOperations(n):
    """
       calculates the fewest number of operations needed
       to result in exactly n H characters in the file
    """
    if (n <= 1):
        return 0
    least_power = int(math.log(n, 2))

    if (2 ** least_power == n):
        return least_power * 2

    elif (n % 2 != 0):
        return 0
    else:
        least_square = math.gcd(2 ** least_power, n)
        return int(2 * math.log(least_square, 2) + (n / least_square))
