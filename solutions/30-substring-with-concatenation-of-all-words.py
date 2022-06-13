# s => len(s)
# n => len(words)
# w => len(words[0])

# O(snw - (nw)^2) time | O(n+w) space
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        strLen = len(s)
        numOfWords = len(words)
        wordLen = len(words[0])
        # O(n) time since we store n keys
        needed = collections.Counter(words)
        
        # O(n + nw) = O(nw)
        def validWindow(start):
            # O(n) time
            # O(n) space but since the copy is destroyed after this function, O(2n) space at max => O(n) space
            neededCopy = needed.copy()
            
            # O(n) time
            for i in range(numOfWords):
                startWord = start + wordLen*i
                # O(w) time | O(w) space
                word = s[startWord:startWord+wordLen] 
                
                # if word is not needed -> return false
                if not neededCopy[word]:
                    return False
                neededCopy[word] -= 1
            
            return True
                
        # we call validWindow s - nw times
        # expanded to O((s-nw) x nw) = O(snw - (nw)^2)
        return [idx for idx in range(strLen - numOfWords*wordLen + 1) if validWindow(idx)]