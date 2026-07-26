class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        n = len(prices)
        l = 0
        r = 1
        max_diff = 0

        while r < n:
            curr = prices[r] - prices[l]
            if curr <= 0:
                l = r
                r += 1
                continue
            
            elif curr > max_diff:
                max_diff = curr
                r += 1
                continue

            else:
                r += 1

        return max_diff


            

        