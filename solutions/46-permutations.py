# O(n*n!) time | O(n!) space
# n! leaves in backtrack tree
# n calls to generate n! leaves
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        def getResult(currArr, options):
            if len(currArr) == len(nums):
                results.append(currArr)
                return
            
            for idx, num in enumerate(options):
                getResult(currArr+[num], options[:idx] + options[idx+1:])
        
        getResult([], nums)
        return results
            