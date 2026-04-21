class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buypoint, maxProfit = float('inf'), 0

        for price in prices:

            if price < buypoint:
                buypoint = price

            maxProfit = max(maxProfit, price - buypoint)

        return maxProfit

