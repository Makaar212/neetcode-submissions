class Solution:
    def jump(self, nums: List[int]) -> int:
        # We're always garunteed an answer so that means that we we always have an array

        # we're returning min jumps

        # if len nums empty return nothing
        # if 1 return 0

        

        dp = [float('inf')] * len(nums)

        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            end = min(i + 1 + nums[i], len(nums))
            for j in range(i + 1, end):
                dp[i] = min(dp[i], dp[j] + 1)

        return dp[0]
