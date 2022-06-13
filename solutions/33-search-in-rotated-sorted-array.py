# O(logn) time | O(1) space
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        # left == right is when target is found
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid

            # 4,5,6,7,1,2
            # l   m     r
            #
            # if we know mid is in the left sorted portion
            #     if target = mid: return
            #     if target > mid: target is in 7,1,2
            #     if target < mid: target is in 4,5 OR 1,2
            #         *if target <  left: target is in 1,2
            #         *if target >= left: target is in 4,5
            #
            # 4,5,6,0,1,2,3
            # l     m     r  
            # if we know mid is in the right sorted portion
            #     if target = mid: return
            #     if target < mid: target is in 4,5,6
            #     if target > mid: target is in 1,2,3 OR 4,5,6
            #         *if target >  right: target is in 4,5,6
            #         *if target <= right: target is in 1,2,3
            
            # right side sorted
            if nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            # left side is sorted
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1