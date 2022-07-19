# O(n) time | O(1) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        runningProduct = nums[0]
        for idx in range(1, len(nums)):
            res[idx] = runningProduct
            runningProduct *= nums[idx]

        runningProduct = nums[-1]
        for idx in range(len(nums)-2, -1, -1):
            res[idx] *= runningProduct
            runningProduct *= nums[idx]
        
        return res