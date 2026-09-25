class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # input distinct integers
        # target integer
        # return number of combinations 

        # observations, combinations can repeat, i.e 112 121 211 
        # honestly from what it looks like it's just a dfs decision tree where 
        # for every num in nums add and see if we reach base case of exactly equaling target
        dp = {}
        def dfs(i, amount):
            if amount > target:
                return 0
            if amount == target:
                return 1
            if amount in dp:
                return dp[amount]
            res = 0
            for j in range(len(nums)):
                res += dfs(j, amount + nums[j])
            dp[ amount] = res
            return res

        # for bottom up solution start from the base case (target) and build from there

        return dfs(0,0)