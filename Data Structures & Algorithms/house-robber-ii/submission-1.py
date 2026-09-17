class Solution:
    def rob(self, nums: List[int]) -> int:
        # return max amount of robbable money
        # adjacent houses can't be robbed 
        if len(nums) <= 2:
            return max(nums)
        dp = defaultdict(dict)


        def dfs(i, startingPos):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1 and startingPos == 0:
                return 0
            if i in dp and startingPos in dp[i]:
                return dp[i][startingPos]
            dp[i][startingPos] = max(nums[i] + dfs(i + 2, startingPos), dfs(i + 1, startingPos))
            
            return  dp[i][startingPos]
        return max(dfs(0,0), dfs(1, 1))