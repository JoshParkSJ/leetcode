# brute force O(4^(m+n)) time
# for every cell, search the longest increasing path
# for every cell (m+n), there are 4 choices, total is 4^(m+n)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        def dfs(i, j, prev):
            
            # base condition : check "out of boundaries" situation and 
            # also if "current <= previous" then these are invalid conditions. 
            if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
                return 0
            
            # expand and look in all four directions using simple depth first search
            left = dfs(i, j - 1, matrix[i][j])
            right = dfs(i, j + 1, matrix[i][j])
            top = dfs(i - 1, j, matrix[i][j])
            bottom = dfs(i + 1, j, matrix[i][j])
            
            # return max depth of longest increasing path and 
            # plus 1 to consider the current element.
            return max(left, right, top, bottom) + 1
             
        
        # compute the longest increasing path for each element and
        # update the max value as answer.
        ans = -1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, -1))
        return ans

# -----------------------------------
# dp solution
# note that bfs/dfs usually needs a visited set, but since we want increasing sequences, we will not revisit a cell

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # create a dp array of size m * n to store already computed max_increasing_path_length for index (i, j)
        # where 0 <= i < m and 0 <= j < n
        # initialize the dp array by -1 as length of path can only be a whole number. 
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
                return 0
            
            # if dp[i][j] != -1, that means dp[i][j] has been updated by some >= 0 path length.
            # hence directly use it without recomputing and save recursion time and space.
            if dp[i][j] != -1:
                return dp[i][j]
            
            # compute if dp[i][j] = -1 meaning (i, j) still not computed
            left = dfs(i, j - 1, matrix[i][j])
            right = dfs(i, j + 1, matrix[i][j])
            top = dfs(i - 1, j, matrix[i][j])
            bottom = dfs(i + 1, j, matrix[i][j])
            
            # update the dp value after computing path length for index (i , j)
            # so that we can use it next time without recomputation.
            dp[i][j] = max(left, right, top, bottom) + 1
            return dp[i][j]
        
        ans = -1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, -1))
        return ans
