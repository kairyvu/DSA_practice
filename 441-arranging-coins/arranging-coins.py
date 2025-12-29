class Solution:
    def arrangeCoins(self, n: int) -> int:
        def getSum(n):
            return n*(n + 1) // 2

        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            total = getSum(mid)
            if total <= n:
                l = mid + 1
            else:
                r = mid - 1
        return r