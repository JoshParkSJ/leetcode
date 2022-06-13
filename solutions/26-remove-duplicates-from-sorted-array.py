# O(n) time | O(1) space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        prevNum = float("inf")
        
        for idx in range(len(nums)):
            num = nums[idx]
            if prevNum != num:
                nums[k] = num
                prevNum = num
                k += 1
        
        return k