# O(1) time | O(1) space
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            # shift ans to left to make space for new bit, then append the new bit
            #   00000000000000000000000000001100 + 00000000000000000000000000000001
            # = 00000000000000000000000000001101
            ans = (ans << 1) + (n & 1)  
            n = n >> 1                  
        return ans

    # note: 000000001 = 1
    # n & 1 only gets the last bit
    # n & 11 gets the last 2 bits
    
    # n >> 1 will push the last bit out into void
    # then we can process the next bit
    # this is how we can process bits in reverse order

    # extra side note: 32 bit doesn't contain the bit responsible for +/-, 64 bit does