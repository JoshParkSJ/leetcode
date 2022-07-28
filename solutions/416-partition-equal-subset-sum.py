# brute force
# O(2^n) time | O(2^n) space
class Solution:
    def canPartition(self, nums, i = 0, sum1 = 0, sum2 = 0):
        if i >= len(nums): 
        	return sum1 == sum2

        return (self.canPartition(nums, i+1, sum1 + nums[i], sum2) or # try including into subset-1
                self.canPartition(nums, i+1, sum1, sum2 + nums[i]))   # try including into subset-2


# -----------------------------------------------------------------------------------------------------
# 0/1 knapsack solution (bottom-up dp)
# O(nm) time | O(nm) space where n is size of nums and m is sum of nums

# cols <---> are capacity/weight/value
# rows ^ are index
#      |
#      v

# assuming we have array w of weights and array p of profits
# we are trying to maximize the profits by bagging or not bagging a weight (bag can hold x weight)

# dp stores max profit from using up to i index and capacity of w weight
# recurrence relation: dp[i][w] = max(dp[i-1][w], dp[i-1][w-w[i]] + p[i])

# dp[i-1][w]                   don't bag current idx (current weight)
# dp[i-1][w-w[i]] + p[i]       bag current idx (current weight)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        targetSum = sum(nums)
        if targetSum % 2 == 1:
            return False # only even sums can be split in half
        targetSum = targetSum // 2

        # cols represent runningSum, rows represent idx
        # we want a base case of 0 to we can choose to incl/not incl first element
        # incl/not incl logic is the recurrence relation, which needs 1 row above
        dp = [[False for _ in range(targetSum+1)] for _ in range(len(nums)+1)]
        dp[0][0] = True
        
        # first column is 0 since targetSum is 0 and we don't need any nums to make 0
        for i in range(len(nums)+1):
            dp[i][0] = True
        
        for i in range(1, len(nums)+1):
            for j in range(1, targetSum+1):
                dp[i][j] = dp[i-1][j]
                
                if j >= nums[i-1]:                              # recurrence relation
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]] # in t/f form rather than a num
                    
        return dp[len(nums)][targetSum]


# -----------------------------------------------------------------------------------------------------
# memoization solution (top-down dp)
# O(nm) time | O(nm) space where n is size of nums and m is sum of nums
# worst case no calculation used memo -> oh but we can't hash arrays, so dict memos don't work!!

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
		def dfs(nums, currSum) -> bool:
		    if currSum == 0:
		        return True
		    if not nums or currSum < 0:
		    	return False

		    # if check memo here
		    # else memoize here

		    return (dfs(nums[1:], currSum - nums[0]) or
		            dfs(nums[1:], currSum))

        targetSum = sum(nums)
        if targetSum % 2 == 1:
            return False # only even sums can be split in half
        targetSum = targetSum // 2
        memo = {}
        return dfs(nums, targetSum)

# -----------------------------------------------------------------------------------------------------
# subset sum
# O(nm) time | O(m) space where n is size of nums and m is sum of nums
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
    	targetSum = sum(nums)
    	if targetSum % 2 == 1:
    		return False

    	dp = set()
    	dp.add(0)
    	targetSum = targetSum // 2

    	for i in range(len(nums)):
    		nextDp = set()
    		for x in dp:
    			if x + nums[i] == targetSum:
    				return True
    			nextDp.add(x + nums[i])
    			nextDp.add(x)
    		dp = nextDp

    	return targetSum in dp










