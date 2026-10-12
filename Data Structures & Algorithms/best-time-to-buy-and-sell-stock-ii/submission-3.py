class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # understand, 

        # input is an array of integers, this array of integers are stocks. At any given moment you can buy stock, thing is, you can also sell stock on the same day, hoiwever we can only hold one share of stock at once

        # so this means that we can sell every time we have bought something. This is pointing me towards a boolean flag letting me know hey i've bought something

        # we are also trying to find the maximum profit that i can achieve. with all this information combined this means there are multiple paths i can take,

        # for example, buy day 1 sell day 2 or js buy day 2 and sell day one.

        # Seems like recursion. Some things that I can do is probably go up an index every single time, 
        # at every index i either bought today if i can buy or i sold today if i can't buy or i js held


        # so 2 choices per flag, if bought i can sell or hold, if not bought i can buy or hold

        dp = {}
        def dfs(i, bought: bool):
            if i == len(prices):
                return 0
            if (i, bought) in dp:
                return dp[(i, bought)]
            res = dfs(i + 1, bought)
            if bought:
                sold = dfs(i + 1, not bought) + prices[i]
                res = max(sold, res)
            else:
                buy = dfs(i + 1, not bought) - prices[i]
                res = max(buy, res)
            dp[(i, bought)] = res
            return res
        return dfs(0, False)