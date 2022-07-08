# O(n) time | O(n) space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s:
            char = c.lower()
            if char in "abcdefghijklmnopqrstuvwxyz0123456789":
                chars.append(char)
        
        formattedStr = "".join(chars)
        formattedStrLen = len(formattedStr)
        left = (formattedStrLen // 2)-1
        right = left+1 if formattedStrLen % 2 == 0 else left+2
        while left >= 0 and right <= formattedStrLen-1:
            if formattedStr[left] != formattedStr[right]:
                return False
            left -= 1
            right += 1

        return True


# O(n) time | O(n) space
class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list
