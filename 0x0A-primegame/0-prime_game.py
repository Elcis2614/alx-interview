#!/usr/bin/python3
""" Prime Game Algorithm"""

MYPRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
            61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
            131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
            193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
            263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331,
            337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
            409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
            479, 487, 491, 499]


def primeCount(n: int) -> int:
    """
        Returns the number of prime numbers
        from 1 to n
    """
    for i in range(len(MYPRIMES)):
        if MYPRIMES[i] > n:
            break
    return len(MYPRIMES[:i])


def isWinner(x: int, nums: [int]) -> [str, type(None)]:
    """
        Return the winner
    """
    if nums is None:
        return None
    if type(x) == int and x > 0 and x <= len(nums):
        Maria = 0
        Ben = 0
        for n in nums:
            if (type(n) is not int) or (n <= 0):
                return None
            else:
                count = primeCount(n)
                if count % 2 == 0 or n == 1:
                    Ben += 1
                else:
                    Maria += 1
        if Maria > Ben:
            return "Maria"
        elif Ben > Maria:
            return "Ben"
    return None
