# O(n) time | O(n) space
class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []
        
        for bracket in s:
            if bracket in '{[(':
                stack.append(bracket)
            elif not stack or mapper[bracket] != stack.pop():
                return False
        
        return len(stack) == 0