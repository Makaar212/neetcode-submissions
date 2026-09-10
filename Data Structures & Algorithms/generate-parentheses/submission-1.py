class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # base case, n = 0
        # this is similar to permutations problem where we have to generate valid permutations, 
        

        # constraints, parenthesis must be well formed, for every '('  there must be a ')'

        # how to take a step

        # backtrack

        res = []
        cur = []
        def dfs(openP, closeP):
            if openP == closeP == n:
                res.append("".join(cur))
                return 
            if openP < n:
                cur.append('(')
                dfs(openP + 1, closeP)
                cur.pop()
            if closeP < openP:
                cur.append(')')
                dfs(openP, closeP + 1)
                cur.pop()
        dfs(0, 0)
        return res

        