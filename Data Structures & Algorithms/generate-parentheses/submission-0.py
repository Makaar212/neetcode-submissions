class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # base case, n = 0
        # this is similar to permutations problem where we have to generate valid permutations, 
        

        # constraints, parenthesis must be well formed, for every '('  there must be a ')'

        # how to take a step

        # backtrack

        res = []
        def dfs(openP, closeP, cur):
            if openP < closeP:
                return 
            if openP > n:
                return 
            if len(cur) == 2 * n:
                res.append(cur[:])
                return
            
            cur += '('
            dfs(openP + 1, closeP, cur)
            cur = cur[:-1]
            cur += ')'
            dfs(openP, closeP + 1, cur)
            print( cur)
        dfs(1, 0, '(')
        return res

        