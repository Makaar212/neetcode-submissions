class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)

        dp[-1] = 0
        for i in range(amount - 1, -1, -1):
            for coin in coins:
                if i + coin <= amount:
                    dp[i] = min(dp[i], 1 + dp[i + coin])
        if dp[0] == float('inf'):
            return -1
        else:
            return dp[0]