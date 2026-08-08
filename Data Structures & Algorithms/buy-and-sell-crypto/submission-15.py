class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L, R = 0, 1
        while R < len(prices):
            profit = prices[R] - prices[L]
            if L == R:
                R += 1
            elif prices[L] > prices[R]:
                L = R
            else:
                R += 1
            res = max(profit, res)
        return res
        