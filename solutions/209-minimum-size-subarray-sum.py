# O(n) time | O(1) space
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        currSum = 0
        windowLen = float("inf")
        
        for end, endVal in enumerate(nums):
            currSum += endVal
            while currSum >= target:
                windowLen = min(windowLen, end - start + 1)
                currSum -= nums[start]
                start += 1
                
        return windowLen if windowLen != float("inf") else 0
