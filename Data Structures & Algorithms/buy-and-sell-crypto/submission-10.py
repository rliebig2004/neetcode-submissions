class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for i, price in enumerate(prices):
            if i == 0:
                continue
            
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
        