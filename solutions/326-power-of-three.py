# O(logn) time with base 3 | O(1) space
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            n /= 3
        return int(n) == 1