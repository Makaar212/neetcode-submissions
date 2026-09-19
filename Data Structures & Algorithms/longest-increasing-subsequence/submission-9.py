class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i] and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1
                    res = max(res, dp[i])
        return res