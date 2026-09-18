class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # input a list of differnt coins that we have 
        # and the target amount we must reach

        # output, the amount of coins it would take to get to target
        # edge if coins can't equal target
        # if coins are negative
        # no amount
        

        # dfs should return amount of coins dfs(n) takes
        dp = {}
        def dfs(running, currCoins):

            if running == amount:
                return 0
            if running in dp:
                return dp[running]
            if running > amount:
                return float('inf')
            res = float('inf')

            for coin in coins:
                res =  min(res, 1 + dfs(running + coin, currCoins + 1))
            dp[running] = res
            return res
        res = dfs(0,0)
        if res == float('inf'):
            return -1
        else:
            return res