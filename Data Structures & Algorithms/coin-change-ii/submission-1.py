class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # amount can be 0 
        # amount and coins can't be negative 
        # coins will always have at least one element
        # coins[i] min is 1 max is 5000

        # Observations:
            # Many different paths
            # each path has to be unique
            # recursively 
            # Brute Force:
                # is valid path, 1
                    # if running amount == 0
                # if not then return 0, 
                    # running > amount 
        dp = {}
        def dfs(i, a):
            if a == 0:
                return 1
            if i >= len(coins) or a < 0:
                return 0
            if (i, a) in dp:
                return dp[(i, a)]
            res = 0
            res = dfs(i + 1, a)
            res += dfs(i, a - coins[i])

            dp[(i, a)] = res
            return res
        
        return dfs(0, amount)


        
