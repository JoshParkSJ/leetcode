# O(n * n^4) time | O(n^4) space
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        result = []
        
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                result.append(currStr)
                return
            
            for char in mapping[digits[i]]:
                backtrack(i+1, currStr + char)
        
        if digits:
            backtrack(0, "")
                        
        return result
    
    
