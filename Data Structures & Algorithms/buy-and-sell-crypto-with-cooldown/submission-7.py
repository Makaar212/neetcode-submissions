class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # only allowed to own one neetcoin at a time

        # if there is an array of len 1, you can't make profit

        if len(prices) <= 1:
            return 0
        dp = {}
        
        
        
        def dfs(i, bought: bool):
            if i >= len(prices):
                return 0
            if (i, bought) in dp:
                return dp[(i, bought)]              

            res = max(dfs(i + 1, bought), 0)
            if bought:
                res = max(res, dfs(i + 2, not bought) + prices[i])
            else:               
                res = max(res, dfs(i + 1, not bought) - prices[i])
            
            dp[(i, bought)] = res
            return res
        
        return dfs(0, False)



