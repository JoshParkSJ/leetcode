# O(n^2 * logn) time | O(1) space
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]

                if currSum >= target:
                    right -= 1
                else:
                    temp = right
                    right -= 1
                    result += 1
                    while right != left:
                        right -= 1
                        result += 1
                    left += 1
                    right = temp
        
        return result
                        
                    
                    
        
        