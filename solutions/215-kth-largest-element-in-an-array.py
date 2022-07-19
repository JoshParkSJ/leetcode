# O(n) avg time O(n^2) worst case when arr is already sorted | O(n) space
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quickselect(left, right):
            pivot, p = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p] # swap(nums[p], nums[i])
                    p += 1
            nums[p], nums[right] = nums[right], nums[p] # swap(nums[p], pivot)
            
            if p > k:                         # [,_,k,_,_,p,_]
                return quickselect(left, p-1)
            elif p < k:                       # [,_,p,_,_,k,_]
                return quickselect(p+1, right)
            else:
                return nums[p]
                
        return quickselect(0, len(nums)-1)