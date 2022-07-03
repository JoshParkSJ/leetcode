# O(n*2^n) time
#   - exist or nonexist for every digit => O(2^n)
#   - create subsets of size 1 to n => O(n)
# O(n) space
#   - depth of recursion stack

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, [], result)
        return result
    
    def backtrack(self, nums, combination, result):
        # key diff from bottom sln here <--------------------------------------------------
        # we also want the subsets made during the process of creating n size combination
        result.append(combination)

        for idx in range(len(nums)):
            self.backtrack(nums[idx+1:], combination+[nums[idx]], result)






# ---------------------same concept, slower

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[], nums]
        combination = []
        for size in range(1, len(nums)):
            self.backtrack(nums, combination, result, size)
        return result
    
    def backtrack(self, nums, combination, result, size):
        if len(combination) == size:
            result.append(combination)
            return
        
        for idx in range(len(nums)):
            self.backtrack(nums[idx+1:], combination+[nums[idx]], result, size)
