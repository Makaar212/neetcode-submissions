class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {target : 1}

        for i in range(target, -1, -1):
            for num in nums:
                dp[i] = dp.get(i + num, 0) + dp.get(i, 0)
        return dp[0]