class Solution:
    def minMoves(self, balance: List[int]) -> int:
        negativeIndex = -1
        total = 0
        remaining = -1
        n = len(balance)

        for i, num in enumerate(balance):
            if num < 0:
                negativeIndex = i
                remaining = -num
            total += num
        
        if negativeIndex == -1:
            return 0
        
        if total < 0:
            return -1
        
        res = 0
        diff = 1
        while remaining > 0:
            left, right = (negativeIndex - diff) % n, (negativeIndex + diff) % n
            l, r = balance[left], balance[right]
            if left == right:
                res += remaining * diff
                remaining -= l
            else:
                res += min(remaining, l + r) * diff
                remaining -= (l + r)
            diff += 1
        return res
            