# O(n) time | O(1) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, num, ...]
        for num in nums:
            # skip rob2 or skip n
            temp = max(rob1 + num, rob2)
            rob1 = rob2 # we could store these in an array and just get currIdx - 1 and -2
            rob2 = temp # but this is more efficient
        return rob2
    
    # [rob1, rob2, num, ...]
    # recurrence relation: we can rob current house OR we can skip current house
    #   - rob current: rob1 + num (rob1 is the sum of robbed houses from [all here, X, +now])
    #   - skip current: rob2 (rob2 is the sum of robbed houses from [all here, Xnow])