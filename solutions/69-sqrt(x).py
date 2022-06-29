# O(logn) time | O(1) space
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        
        # while left < right: set right = mid
        # while left <= right: set right = mid-1
        while left <= right:
            mid = (left + right) // 2
            expo = mid*mid
            
            if expo > x:
                right = mid-1
            elif expo < x:
                left = mid+1
            else:
                return mid
        
        return right if x >= 2 else x 
        