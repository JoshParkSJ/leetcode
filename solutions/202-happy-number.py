# O(1) time | O(1) space
# integer max value = 2 147 483 647 (assuming 32 bit), which has a sum of squares 260
# then the number that would give us the max sum of squares is 1 999 999 999, which has a sum of squares 724
# Therefore, any valid integer would give us a sum of squares in the range [1,724] meaning that we would 
# at most need 724 iterations before reaching a repeat or 1
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n not in visited:
            visited.add(n)
            
            sumOfSquares = 0
            for digit in str(n):
                sumOfSquares += (int(digit) * int(digit))
            
            if sumOfSquares == 1:
                return True
            
            n = sumOfSquares
        
        return False
            