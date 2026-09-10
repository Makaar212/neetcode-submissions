class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # this is similar to subset, however this one has dupes. 

        # the constraint of this is not to return duplicate subsets. 

        # time comp allows for sorting. 

        # decision tree is js add or not to add 
        # base case if i >= len nums
        nums.sort()
        res = []
        def dfs(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return 
            cur.append(nums[i])
            dfs(i + 1, cur)

            cur.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, cur)
        dfs(0, [])
        return res
        