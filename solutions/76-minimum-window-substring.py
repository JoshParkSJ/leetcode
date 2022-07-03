class Solution:
    def minWindow(self, s: str, t: str) -> str:
        neededChars = collections.Counter(t)
        neededLen = len(t)
        windowStart = windowEnd = 0
        i = 0
        
        # emuerate start=1, just so we don't have to return s[windowStart:windowEnd+1]
        # we are NOT skipping an idx, we still iterate the same amount but starting from idx 1
        # python slicing excludes last index
        for j, char in enumerate(s):
            if neededChars[char] > 0: 
                neededLen -= 1
            neededChars[char] -= 1
            
            if neededLen == 0:
                # if neededChars is negative, that's not a character we need (not part of t)
                # shrink window if it's still valid
                while neededChars[s[i]] < 0:
                    neededChars[s[i]] += 1
                    i += 1

                # first window OR smaller window exists
                if windowEnd == 0 or windowEnd - windowStart > j - i:
                    windowEnd = j
                    windowStart = i

                neededChars[s[i]] += 1
                neededLen += 1
                i += 1
        
        return s[windowStart:windowEnd]
        