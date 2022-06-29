
# O(mn) time | O(mn) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)] # O(mn) space
        
        for i in range(m): # O(m) time
            for j in range(n): # O(n) time
                if i == 0 or j == 0:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]


    # 1  1  1  1
    # 1  2  3  4
    # 1  3  6  10 <- answer
    # box = box's up + box's left

        

# --------------------------------------------------------

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # start from bottom row
        
        for i in range(m-1): # all rows except bottom row
            newRow = [1] * n # row above bottom row
            for j in range(n - 2, -1, -1): # last column is 1 anyways
                newRow[j] = newRow[j+1] + row[j] # right val + old/bot row's val
            row = newRow
        
        return row[0]
        
        
    # s  21  15  10  6  3  1
    # 7   6   5   4  3  2  1
    # 1   1   1   1  1  1  1 <- we choose to define target as 1
    # every box is the sum of right and down



