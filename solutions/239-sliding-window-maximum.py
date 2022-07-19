# O(n) time | O(n) space
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = right = 0
        result = []
        queue = deque() # monotonically decreasing [8,7,6,5...]
        
        while right < len(nums):
            # load up next biggest num into window (kick out numbers smaller than curr)
            # every popleft() will leave next biggest num in window
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
    
            queue.append(right)
            
            if left > queue[0]: # idx is no longer in window
                queue.popleft()
                
            if (right+1) >= k: # start adding to result only when window size is k 
                result.append(nums[queue[0]])
                left += 1
                
            right += 1
            
        return result