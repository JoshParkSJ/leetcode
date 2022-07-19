# O(1) time | O(1) space
class Solution:
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (n - 1) == 0

# ------------------------------

# O(logn) time | O(1) space
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            n /= 2
        return n == 1