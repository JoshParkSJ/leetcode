# O(ca) time where c is the amount of coins | O(a) space where a is the target amount
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for am in range(1, amount+1):
            for coin in coins:
                if am - coin >= 0:
                    dp[am] = min(dp[am-coin] + 1, dp[am])
                    
        
        return dp[amount] if dp[amount] != float("inf") else -1