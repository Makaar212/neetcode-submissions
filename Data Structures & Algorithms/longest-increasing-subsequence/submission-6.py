class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = {}
        def dfs(i):
            if i >= len(nums):
                return 1
            if i in dp:
                return dp[i]
            res = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(1 + dfs(j), res)
            dp[i] = res
            return res
        
        best = 1
        for i in range(len(nums)):
            best = max(best, dfs(i))
        return best