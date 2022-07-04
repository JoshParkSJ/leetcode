# dp tabulation (bottom-up)
# O(mn) time | O(mn) space
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): 
            return False

        dp = [ [False]*(len(s2) + 1) for i in range(len(s1) + 1) ]
        dp[len(s1)][len(s2)] = True
        
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):

                # one of the strings could be out of bound while the other is not
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]



# -----------------------------------------------------------------


# memoization (top-down)
# if we don't use cache -> O(2^n+m) brute force time
# O(nm) time | O(n+m) space

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): 
        return False
        
        cache = {}
        # k = i + j
        def dfs(i,j):
            # out of bound
            if i == len(s1) and j == len(s2):
                return True
            if (i,j) in cache:
                return cache[(i,j)]
            
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                return True
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True
            cache[(i,j)] = False
            return False
        return dfs(0,0)
    

