# O(32 or 1) time | O(1) space
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift
    
    # purely using the fact that there will only be 1 common bit
    # shift left until we get to which bit is that common bit (i.e 2^6 would mean 6 shifts)
    # at the end, we just shift back to original position
    
    # idea 1: & will make everything into a 0 unless it's a 1&1 (could also not exist at all where every num in range lines up to 1&1)
    # idea 2: if right == left that means we've reached 000001 and 000001, how many times we shifted to get to this point is the bit that lines up 1&1


# ----------------------

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # turn off rightmost 1-bit
            n = n & (n - 1)
        return m & n

# when we do n & n-1, the rightmost bit of one in the original number would be turned off 
# i.e 000100101
# to  000100000

# note: subtraction and addition on bits work the same way as base 10, except carry overs are in 2's
# 12:        00001100
# 11:        00001011
# n & (n-1): 00001000
