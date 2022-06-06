# O(n) time | O(n) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        
        for idx in range(len(nums)):
            num = nums[idx]
            potentialNum = target - num
            
            if potentialNum in visited:
                return [visited[potentialNum],idx]
            
            visited[num] = idx
        
        return -1