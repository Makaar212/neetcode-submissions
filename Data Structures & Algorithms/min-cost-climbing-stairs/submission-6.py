class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n

        # iterate through the array backwards
            # cost of cur is cost[cur] + min(cur + 1, cur + 2) 
        for i in range(n - 1, -1, -1 ):
            if i + 2 >= n:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        print(dp)
        return min(dp[0], dp[1])