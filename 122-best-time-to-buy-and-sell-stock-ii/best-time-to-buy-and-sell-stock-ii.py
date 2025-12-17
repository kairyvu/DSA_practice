class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowestPrice = float("inf")
        n = len(prices)

        for i, p in enumerate(prices):
            if p < lowestPrice:
                lowestPrice = p
                continue
            else:
                if i + 1 < n:
                    if prices[i + 1] < p:
                        res += p - lowestPrice
                        lowestPrice = prices[i + 1]
                else:
                    res += p - lowestPrice
        return res