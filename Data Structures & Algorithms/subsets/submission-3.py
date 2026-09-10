class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, cur):
            
            if i >= len(nums):
                res.append(cur.copy())
                return 
            
            # Decision 1: include
            cur.append(nums[i])
            dfs(i + 1, cur)

            # decision 2: don't include
            cur.pop()
            dfs(i + 1, cur)
        dfs(0, [])
        return res