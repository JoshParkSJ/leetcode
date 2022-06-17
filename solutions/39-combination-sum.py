# O(2^t) time where t is target | O(t) space
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.dfs(candidates, target, [], results)
        return results
    
    def dfs(self, nums, target, path, results):
        if target < 0:
            return 
        if target == 0:
            results.append(path)
            return 
        
        # decision tree with 2 decisions every node:
        #   include i, don't include i/only include i+1 onwards
        # O(2^t) because worst case we add 1 t times to get to t
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], results)