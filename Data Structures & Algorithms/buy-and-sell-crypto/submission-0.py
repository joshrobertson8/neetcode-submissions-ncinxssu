class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minIdx, maxProfit = prices[0], 0

        for i in range(1, len(prices)):
            if prices[i] < minIdx:
                minIdx = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - minIdx)

        return maxProfit