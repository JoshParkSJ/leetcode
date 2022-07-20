# O(n) time | O(n) space
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordDict = {}
        patternsUsed = set()
        patternIdx = 0
        arrayStr = s.split()
        
        for word in arrayStr:
            if word not in wordDict:
                if patternIdx >= len(pattern) or pattern[patternIdx] in patternsUsed:
                    return False
                wordDict[word] = pattern[patternIdx]
                patternsUsed.add(pattern[patternIdx])
                patternIdx += 1
            elif patternIdx >= len(pattern) or wordDict[word] != pattern[patternIdx]:
                return False
            else:
                patternIdx += 1
        
        print(patternIdx)
        return patternIdx == len(pattern)

        
        