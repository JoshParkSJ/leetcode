# O(n^3) time | O(n^2) space
class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        numsLen = len(nums) + 2
        dp = [[0] * numsLen for _ in range(numsLen)]
        
        for i in range(numsLen - 2, -1, -1):
            for j in range(i + 2, numsLen):
                for k in range(i+1, j):
                    dp[i][j] = max(nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        
        return dp[0][numsLen-1]

# we fill up dp for boundaries of length 1 first: 
# - [0,0], [1,1], [2,2], [3,3]
# then length 2:
# - [0,1], [1,2], [2,3]
# then length 3:
# - [0,2], [1,3]
# then length 4:
# - [0,4]

# we use k as the last balloon to be popped
# imagine i,j boundary has this: [a,b] + [k] + [c,d]
# we can use dp[a][b] and dp[c][d] to find what the max value for popping these ranges would be
# if [a,b] or [c,d] is out of bound from i,j, then they would be 0 since we set the dp table to 0 initially
# for the actual k balloon popping and calculating the coins for this operation
# - look at i-1 and j+1 since k is supposed to be the last balloon to be popped, everything else within i,j range should be popped already
# - if i-1 and j+1 goes out of bound of the actual nums array, there is a 1 which is what the question asks us to do (multiply by 1)

# example
# 3,1,5,8
#   i j

# k is at 1
# pop k => 3 * 1 * 8
