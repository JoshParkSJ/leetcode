# O(mn^2) time | O(n) space
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        # O(n) time
        for i in range(len(s)-1, -1, -1):
            # O(m) time
            for word in wordDict:
                # O(n) time worst case
                if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break
        
        return dp[0]