class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # duplicate input, can only be chosen once


        # goal: get all combinations that equal target
        # constraints: output must be unique, counted by freq
        # base case: if total > target, if i is out of bounds, 
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return 
            
            # Decision 1: include curr number
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            
            # Decision 2: don't include curr number, avoid dupes
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res