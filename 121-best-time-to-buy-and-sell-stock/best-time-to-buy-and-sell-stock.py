class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slowestBuy = float("inf")
        res = 0

        for p in prices:
            if p < slowestBuy:
                slowestBuy = p
                continue
            res = max(res, p - slowestBuy)
        return res