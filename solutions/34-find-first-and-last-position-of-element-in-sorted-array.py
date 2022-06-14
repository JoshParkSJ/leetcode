class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            lo, hi = 0, len(nums)  
            
            # only ends if lo == hi
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    # target exists: ensures lo is at leftmost idx of target
                    # target dne:    ensures lo is indexed higher than target (oob or num)
                    # i.e) mid+1 and onwards contains target
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
        
        return [-1, -1]
    
    
# search function
#    find the lowest idx of target
#         if there is target num in nums
#             lo = lowest index of target
#             hi = lowest index of target
#         if target dne
#             if there's a num > target 
#                 lo = leftmost idx with first num bigger than target 
#                 hi = leftmost idx with first num bigger than target 
#             else
#                 lo = len(nums)
#                 hi = len(nums)
                
# after lo = search(target), hi = search(target+1) -1
# if lo == high: 1 target
# if lo < high: lo is leftmost idx of target, hi is rightmost of idx of target
# if lo > high:
#       if there's a num > target: 
#             lo = leftmost idx of first num bigger than target
#             hi = leftmost idx of first num bigger than target - 1
#       else:
#             lo = len(nums)
#             hi = len(nums)-1