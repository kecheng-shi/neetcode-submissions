class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit = 0
        min = float("inf")

        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min)
        
        return max_profit