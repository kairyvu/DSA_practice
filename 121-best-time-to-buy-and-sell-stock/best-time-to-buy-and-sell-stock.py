class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slowestBuy = float("inf")
        res = float("-inf")

        for p in prices:
            if p < slowestBuy:
                slowestBuy = p
                continue
            res = max(res, p - slowestBuy)
        return res if res != float("-inf") else 0