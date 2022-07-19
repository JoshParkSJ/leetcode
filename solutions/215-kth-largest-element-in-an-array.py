# O(n) avg time O(n^2) worst case when arr is already sorted | O(n) space
# quick select
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quickselect(left, right):
            pivot, p = nums[right], left # set pivot to end
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p] # left part of array <= pivot/end
                    p += 1         
            nums[p], nums[right] = pivot, nums[p] # pivot is actually nums[right]. Right part of array is now > pivot/end
            
            if p > k: 
                # left portion of array
                return quickselect(left, p-1)
            elif p < k:
                # right portion of array
                return quickselect(p+1, right)
            else:
                return nums[p]
                
        return quickselect(0, len(nums)-1)