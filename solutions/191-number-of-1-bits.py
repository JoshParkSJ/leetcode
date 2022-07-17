# O(1) time | O(1) space
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            if n & 1 == 1:
                res += 1
            n = n >> 1
        return res


# -------------------

# 1000000001  n
# 1000000000  n-1
# 1000000000  n & (n-1)    res = 1

# 1000000000  n
# 0111111111  n-1
# 0000000000  n & (n-1)    res = 2

# O(1) time | O(1) space
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        while n:
            n = n & (n-1)
            res += 1
            
        return res

# note: subtraction and addition on bits work the same way as base 10, except carry overs are in 2's
# 12:        00001100
# 11:        00001011
# n & (n-1): 00001000