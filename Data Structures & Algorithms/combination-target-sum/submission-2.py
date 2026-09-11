class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # distinct input, can be used morethan once
        # distinct output, checked with freq
        # return all combinations that equal target

        # base case, greater than target, out of bounds, 
        # constraints, can be used morethan once, distinct output
        # choice, include this one or don't include this one


        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i >= len(nums):
                return
            
            # Decision 1: include current
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # Decision 2: don't inlcude current
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res