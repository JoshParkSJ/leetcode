# for num > 2, it is always 1 < num/2 < sqrt(num)
# O(logn) time | O(1) space
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left, right = 2, num
        while left <= right:
            mid = (left + right) // 2
            potentialSquare = mid*mid
            
            if potentialSquare > num:
                right = mid - 1
            elif potentialSquare < num:
                left = mid + 1
            else:
                return True
        
        return False