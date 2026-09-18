class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # iterate through the array backwards
            # cost of cur is cost[cur] + min(cur + 1, cur + 2) 
        for i in range(n - 1, -1, -1 ):
            if i + 2 >= n:
                cost[i] = cost[i]
            else:
                cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])
        print(cost)
        return min(cost[0], cost[1])