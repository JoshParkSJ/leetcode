# bottom up dp
# O(n) time | O(n) space
class Solution:
    def numDecodings(self, s): 
        if not s or s[0] == 0: return 0
        if s[0] == 0: return 0

        dp = [0 for x in range(len(s) + 1)] 
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, len(s) + 1):     
            if 0 < int(s[i-1:i]) <= 9: # One step jump
                dp[i] += dp[i - 1]
        
            if 10 <= int(s[i-2:i]) <= 26: # Two step jump
                dp[i] += dp[i - 2]

        return dp[len(s)]
    
# 1
# - 1

# 12
# - 1 2
# - 12

# 121
# - 1 2 1
# - 1 21
# - 12 1

# 1212
# - 1 2 1 2 <-- 121 + 2
# - 1 21 2 <-- 
# - 12 1 2 <-- 
# - 1 2 12 <-- 12 + 12
# - 12 12 <--

# the last digit added "2" for 1212 can be interpreted as 2 or 12
# f(n-1) so we can take account for 1 more digit (2)
# f(n-2) so we can take account for 2 more digits (12)


# ----------------------- memoization (top-down dp)

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s): 1 }
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            result = dfs(i+1)
            if (i+1 <= len(s) - 1 and 
                (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                result += dfs(i+2)
            dp[i] = result
            return result
        
        return dfs(0)