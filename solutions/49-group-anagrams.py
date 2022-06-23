class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for str in strs:
            sortedStr = ''.join(sorted(str))
            if sortedStr in anagrams:
                anagrams[sortedStr].append(str)
            else:
                anagrams[sortedStr] = [str]
        
        return list(anagrams.values())
            