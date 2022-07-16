# O(n) time | O(1) space, at most 3 elements
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = 0
        longestSubstr = 0
        charsInWindow = {}
        
        for endIdx, endChar in enumerate(s):
            charsInWindow[endChar] = endIdx
            
            if len(charsInWindow) > 2:
                leftMostIdx = min(charsInWindow.values())
                del charsInWindow[s[leftMostIdx]]
                start = leftMostIdx + 1

            # key difference from min vs max sliding window
            # as long as there's 2 chars in the window
            # we can continuously update the max
            longestSubstr = max(longestSubstr, endIdx - start+1)    
            
        return longestSubstr