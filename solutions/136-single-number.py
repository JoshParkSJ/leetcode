# O(n) time | O(1) space
# XOR is associative (A ^ B) ^ C == A ^ (B ^ C)
# 0 ^ 2 ^ 1 ^ 4 ^ 5 ^ 2 ^ 4 ^ 1
# 0^ 2^2 ^ 1^1 ^ 4^4 ^5 (Rearranging, taking same numbers together)
# 0 ^ 0 ^ 0 ^ 0 ^ 5
# 0 ^ 5
# 5 :)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # 0 is a good default value because n ^ 0 = n where ^ is XOR
        for num in nums:
            res = res ^ num
        return res