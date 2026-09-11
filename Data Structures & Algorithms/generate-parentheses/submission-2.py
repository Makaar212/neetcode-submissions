class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # The parenthesis must be well formed, meaning for every open there must be a close and no close can come before open
        # what does that mean, that means the amount of close P must alway sbe <= open p. before we can add any clsoe P close < openP
        # base case, when there is enough closeP and openP that it equals 2 * n, or openP is greater than n 

        res = []

        def dfs(openP, closeP, cur):
            if openP > n:
                return 
            if closeP > openP:
                return 
            if openP == closeP == n:
                res.append(''.join(cur))
                return
            
            if closeP < openP:
                cur.append(')')
                dfs(openP, closeP + 1, cur)
                cur.pop()
            if openP < n:
                cur.append('(')
                dfs(openP + 1, closeP, cur)
                cur.pop()
        dfs(0,0, [])
        return res
        