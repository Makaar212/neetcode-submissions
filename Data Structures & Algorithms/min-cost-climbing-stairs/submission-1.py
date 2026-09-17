class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # check the next two options, 
        # whichever is less, go with that step
        # if n + 2 is out of bounds, return res += current n 
        # if n == len(cost) - 1, we are there. if n + 2 == len(cost) we are there

        # n + 2 == len(cost)
        # n + 2 is out of bounds, res += cost[n]
        # check whatever is min
        res = 0
        dp = {}
        def dfs(n):
            
            if n >= len(cost):
                return 0
            if n in dp:
                return dp[n] 
            dp[n] = cost[n] + min(dfs(n + 1), dfs(n + 2))
            return dp[n]
        return min(dfs(0), dfs(1))
