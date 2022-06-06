# O(n) time | O(n) space
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chars = set()
        max_count = 0
        
        for right in range(len(s)):
            curr_char = s[right]
            
            while curr_char in chars:
                chars.remove(s[left])
                left += 1
            
            chars.add(curr_char)
            max_count = max(right - left + 1, max_count)
        
        return max_count
        