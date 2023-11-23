#!/usr/bin/python3
"""
    Program algorithm implimentation
"""


def makeChange(coins, total):
    """
        Entry function
    """
    if total <= 0:
        return 0
    coins.sort()
    if total == coins[0]:
        return 1
    remainder = total
    num = 0
    for i in range(-1, -(len(coins)) - 1, -1):
        if remainder == 0:
            break
        if remainder % coins[i] == 0:
            num += int(remainder / coins[i])
            break
        else:
            factor = int(remainder / coins[i])
            num += factor
            remainder = remainder % coins[i]
    else:
        return -1
    return num
