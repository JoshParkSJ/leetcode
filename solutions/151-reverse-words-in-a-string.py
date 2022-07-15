# O(n) time | O(n) space
class Solution:
    def reverseWords(self, s: str) -> str:
        splitWords = []
        strippedWords = s.strip()
        prevChar = None
        start = 0
        for idx, char in enumerate(strippedWords):
            if prevChar == " ":
                start = idx
    
            if char == " ":
                if prevChar and prevChar != " ":
                    splitWords.append(strippedWords[start:idx])
                
            prevChar = char
        
        splitWords.append(strippedWords[start:len(strippedWords)])
        return " ".join(reversed(splitWords))
        