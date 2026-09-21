class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # inputs:
            # Array of nums that we can choose to  add or subtract
            # can we only use each num once? yes
            # can target be negative? yes
            # can target be 0? yes
            # because of these things we should prolly add up to target, not go down to 0
            # are inputs proper? yes
            # duplicate numbers? yes
            # return all the paths is the output, so every different path we can take
            # sounds like dfs exploring every path. 

            # we can do this recursively

            # base case would be if we made it to target or if we made it to the end of the nums list

            # at every num we have two choices, either add the current number and move on or subtract the
            # current number and move on, so at every choice we move on

            dp = {}
            
            def dfs(i, amount):
                if i >= len(nums):
                    return amount == target
                if (i, amount) in dp:
                    return dp[(i, amount)]  
                
                res = dfs(i + 1, amount - nums[i]) + dfs(i + 1, amount + nums[i])
                dp[(i, amount)] = res
                return res


            res = dfs(0,0)

            if res == 1 and len(nums) > 1: return 0 
            else: return res