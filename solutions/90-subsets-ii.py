# O(n2^n) time | O(n) space
# O(2^n) time because every digit can exist or not exist
# O(n) time because every subset array be up to length n (and we need time to build that array)
# O(n) space because that's the depth of the recursive track

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.backtrack(nums, [], result)
        return result
    
    def backtrack(self, nums, subset, result):
        result.append(subset)
        if not nums:
            return
        
        prevNum = None
        for idx, num in enumerate(nums):
            if prevNum != num:
                self.backtrack(nums[idx+1:], subset+[num], result)
            prevNum = num


# --------------- 
# iterative solution

class Solution(object):
    def subsetsWithDup(self, nums):
        result = []
        self.dfs(sorted(nums), [], result)
        return result
    
    def dfs(self, nums, path, result):
        result.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # <-------- duplicate check (this trick is also from 3sum)
                continue
            self.dfs(nums[i+1:], path+[nums[i]], result)
