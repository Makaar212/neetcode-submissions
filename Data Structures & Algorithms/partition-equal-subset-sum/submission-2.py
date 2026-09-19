class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        # We can do a dfs function where for every fork, we can either put the number in sub 1 or sub 2
        # instead of using actual arrays we can js use a running coutner for both subsets

        # base cases: when i == len(nums)

        # returns true, and the max of all paths
        dp = {}
        def dfs(i, one, two):
            if i >= len(nums):
                return one == two
            if (one, two) in dp:
                return dp[(one,two)]            
            res = max(dfs(i + 1, one + nums[i], two), dfs(i + 1, one, two + nums[i]))
            dp[(one, two)] = res
            return res
        return dfs(0, 0, 0)