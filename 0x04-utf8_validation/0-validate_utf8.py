#!/usr/bin/python3
"""
    Utf validation function
"""

import re


def leadingByte(n: int) -> int:
    """
        Determine the leading byte
        Return 1 - 4 if correct
        return 0 otherwise
    """
    if (n > int('11110111', 2)):
        return 0
    str_n = '{0:08b}'.format(n)
    if re.search('^11110[0-9]{3}$', str_n):
        return 4
    elif re.search('^1110[0-9]{4}$', str_n):
        return 3
    elif re.search('^110[0-9]{5}$', str_n):
        return 2
    elif re.search('^0[0-9]{7}$', str_n):
        return 1
    return 0


def validUTF8(data):
    """
        Determines if a given data set represents a valid UTF-8 encoding
        Return: True if data is a valid UTF-8 encoding, else return False
    """
    if data is None:
        return False
    elif data == []:
        return True
    bytes_nb = leadingByte(data[0])
    if bytes_nb == 1 or len(data) == 1:
        return True
    elif bytes_nb == 0:
        return True and validUTF8(data[1:0])
    try:
        for i in range(1, bytes_nb):
            if type(data[i]) is not int:
                return False
            str_i = "{0:08b}".format(data[i])
            if data[i] > int('10111111', 2):
                return False
            elif not re.search('10[0-9]{6}', str_i):
                return False
        if len(data) == bytes_nb:
            return True
        return True and validUTF8(data[bytes_nb:])
    except IndexError:
        return False
