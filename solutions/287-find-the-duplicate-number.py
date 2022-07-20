# O(n) time | O(1) space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            fast = nums[fast]
            slow = nums[nums[slow]]
            if fast == slow:
                break
                
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow