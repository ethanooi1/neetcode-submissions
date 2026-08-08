class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L, R = 0, 1
        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                res = max(profit, res)
            else:
                L = R
            R += 1
        return res
        