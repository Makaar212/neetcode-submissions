class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # similar to last problem, 

        # non distinct input

        # distinct output, calculated by freq array,

        # each element may only be chosen once,  similar to 3 sum

        # time comp allows for sorting, 

        # if we sort that allows us to use the next element with no problem 


        # base case, total == target, i >= len(candidates), or total >= target

        # the reason why we need to do a while loop is because we need to watch out for cases like
        # [1,2,1]

        # there is a combination of [1,2] from index 0, 1 and a combination of [2, 1] from index 1,2

        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if total > target or i >= len(candidates):
                return

            # dec 1: include candidates[i]
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            # dec 2: don't include candidates[i] or duplicates

            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, cur, total)
        dfs(0,[], 0)
        return res