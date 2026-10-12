class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        for i in range(len(prices)):
            if i + 1 < len(prices) and prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i] 
        return profit