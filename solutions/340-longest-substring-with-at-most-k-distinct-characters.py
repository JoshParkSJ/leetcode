# O(n) time | O(k) space
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        left = currK = maxLen = 0
        distinctChars = {}
        for right, char in enumerate(s):
            if char not in distinctChars or distinctChars[char] == 0:
                currK += 1
            distinctChars[char] = distinctChars.get(char, 0) + 1
            
            if currK <= k:
                maxLen = max(maxLen, right - left + 1)
            
            if currK > k:
                distinctChars[s[left]] -= 1
                if distinctChars[s[left]] == 0:
                    currK -= 1
                left += 1
            
        return maxLen

# -----------------

# easier, faster, smarter
# O(n) time | O(k) space
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        start = 0
        longestSubstr = 0
        charsInWindow = {}
        for endIdx, endChar in enumerate(s):
            charsInWindow[endChar] = endIdx
            
            if len(charsInWindow) > k:
                leftMostIdx = min(charsInWindow.values())
                del charsInWindow[s[leftMostIdx]]
                start = leftMostIdx + 1

            # key difference from min vs max sliding window
            # as long as there's 2 chars in the window
            # we can continuously update the max
            longestSubstr = max(longestSubstr, endIdx - start+1)    
            
        return longestSubstr