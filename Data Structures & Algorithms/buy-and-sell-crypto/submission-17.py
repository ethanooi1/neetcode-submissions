class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        res = 0
        while R < len(prices):
            if prices[L] > prices[R]:
                L += 1
            else:
                res = max(res, prices[R] - prices[L])
                R += 1

        return res
            
