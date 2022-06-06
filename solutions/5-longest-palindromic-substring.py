# O(n^2) time | O(1) space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPal = s[0]
        
        for idx, char in enumerate(s, 1):
            prevIdx = nextIdx = idx
            
            while (prevIdx - 1 >= 0 and nextIdx + 1 < len(s) and s[prevIdx - 1] == s[nextIdx + 1]):
                prevIdx -= 1
                nextIdx += 1
                                    
            if (nextIdx - prevIdx + 1 > len(longestPal)):
                longestPal = s[prevIdx:nextIdx+1]
        
        for idx, char in enumerate(s):
            prevIdx = nextIdx = idx
            
            while (prevIdx >= 0 and nextIdx + 1 < len(s) and s[prevIdx] == s[nextIdx + 1]):
                prevIdx -= 1
                nextIdx += 1
                                    
            if (nextIdx - prevIdx + 1 > len(longestPal)):
                longestPal = s[prevIdx+1:nextIdx+1]
        
        return longestPal



# cleaner version
class Solution(object):
    def longestPalindrome(self, s):
        res = s[0]

        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
        return res
        
    def helper(self,s,l,r):
        while 0<=l and r < len(s) and s[l]==s[r]:
            l-=1; r+=1
        return s[l+1:r]