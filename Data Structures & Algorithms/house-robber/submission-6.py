class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(n):
            if n >= len(nums):
                return 0
            if n in dp:
                return dp[n]
            dp[n] = max(nums[n] + dfs(n + 2), dfs(n+1))
            return dp[n]
        return dfs(0)