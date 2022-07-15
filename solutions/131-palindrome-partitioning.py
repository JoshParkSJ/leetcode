# O(n2^n) time | O(n) space
# sum of (choose 0 from n-1), (1 from n-1), (2 from n-1), ... (n from n-1), (n-1 from n-1) == 2^(n-1)
# 1 + n-1 + big number + ... + big number + n-1 + 1
# choose k elements from n = all combinations possible with k elements as a group from n elements
# n-1 becase a|b|c|d => 4 chars, 3 groups

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.getPalindromes(s, [], result)
        return result
    
    def getPalindromes(self, string, path, result):
        if not string:
            result.append(path)
            return
        for idx, char in enumerate(string):
            if self.isPalindrome(string[:idx+1]):
                self.getPalindromes(string[idx+1:], path+[string[:idx+1]], result)
                
    def isPalindrome(self, s):
        return s == s[::-1]