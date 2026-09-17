class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)

        # iterate through the array in reverse and see what is the cost of the two choices in front + cur
        res = float('inf')
        for i in range(len(cost) - 1, -1, -1):
            total  = 0

            if i + 2 >= len(cost):
                total = 0 + cost[i]
            else:
                total = cost[i] + min(dp[i + 1], dp[i + 2])
            
            dp[i] = total 
        
        res = min(dp[0], dp[1])
        return res