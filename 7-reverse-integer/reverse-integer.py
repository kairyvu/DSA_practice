class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        signed = 1 if x == abs(x) else -1
        x = abs(x)
        while x > 0:
            digit = x % 10
            res = res*10 + digit
            x //= 10
        if res > 2**31 - 1:
            return 0
        return res * signed