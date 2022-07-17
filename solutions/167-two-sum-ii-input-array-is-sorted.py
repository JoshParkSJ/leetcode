# O(n) time | O(1) space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        
        while left < right:
            numSum = numbers[left] + numbers[right]
            if numSum > target:
                right -= 1
            elif numSum < target:
                left += 1
            else:
                return [left+1, right+1]
            
        return [None, None]