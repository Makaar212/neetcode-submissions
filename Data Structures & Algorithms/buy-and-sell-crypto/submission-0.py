class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            curr = prices[r] - prices[l]
            profit = max(curr, profit)

            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return profit