"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""
import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        if round(math.log(n, 2) % 1, 10) != 0:
            return False
        else:
            return True
