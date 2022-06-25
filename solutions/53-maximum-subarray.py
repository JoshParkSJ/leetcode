# O(n) time | O(1) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxTotal = potentialMax = nums[0]
        for i in range(1, len(nums)):
            potentialMax = max(potentialMax + nums[i], nums[i])
            maxTotal = max(maxTotal, potentialMax)
        return maxTotal