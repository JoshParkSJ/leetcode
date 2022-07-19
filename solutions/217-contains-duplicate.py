# O(n) time | O(n) space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existing_nums = set()
        
        for num in nums:
            if num in existing_nums:
                return True
            else:
                existing_nums.add(num)
        return False