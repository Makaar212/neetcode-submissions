class Solution:
    def jump(self, nums: List[int]) -> int:
        # We're always garunteed an answer so that means that we we always have an array

        # we're returning min jumps

        # if len nums empty return nothing
        # if 1 return 0

        dp = {}


        def dfs(i):
        
            if i >= len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')    
            if i in dp:
                return dp[i]
            res = float('inf')

            for j in range(i + 1, i + nums[i] + 1 ):
                res = min(res, 1 + dfs(j))
            dp[i] = res
            return res

        return dfs(0)
