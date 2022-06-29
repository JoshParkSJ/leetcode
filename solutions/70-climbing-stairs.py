# https://leetcode.com/problems/climbing-stairs/discuss/25313/Python-different-solutions-(bottom-up-top-down)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        arr = [1] * (n+1)
        for i in range(n-2, -1, -1):
            arr[i] = arr[i+1] + arr[i+2]
        return arr[0]

# 0  1step  2step   3step   4step   5step
#[8,   5,     3,      2,      1,       1 ]