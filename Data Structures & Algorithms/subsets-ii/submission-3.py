class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # include or don't include, 
        # base case is i >= nums
        # Assumption, can only use each element once
        res = []
        nums.sort()
        def dfs(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            # Decision 1: include
            cur.append(nums[i])
            dfs(i + 1, cur)
            # Decision 2: don't inlcude avoid dupes
            cur.pop()
            while i  + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, cur)

        dfs(0, [])
        return res