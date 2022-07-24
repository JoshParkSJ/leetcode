# O(n) time | O(1) space
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        
        for i in range(1, n+1):
            count, bit = 0, i
            while bit != 0:
                bit = bit & (bit-1)
                count += 1
            ans[i] = count
        
        return ans


# -----------------

# 0 - 0000 => 0
# 1 - 0001 => 1 = 1 + dp[n-1]
# 2 - 0010 => 1 = 1 + dp[n-2]
# 3 - 0011 => 2 = 1 + dp[n-2]
# 4 - 0100 => 1 = 1 + dp[n-4]
# 5 - 0101 => 2 = 1 + dp[n-4]
# 6 - 0110 => 2 = 1 + dp[n-4]
# 7 - 0111 => 3 = 1 + dp[n-4]
# 8 - 1000 => 1 = 1 + dp[n-8]

# every power of 2, we can use the dp of offset (new offset is current number)
# O(n) time | O(1) space
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp