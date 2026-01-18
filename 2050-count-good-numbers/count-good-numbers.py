class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def power(x, p):
            res = 1
            while p:
                if p & 1:
                    res = (res * x) % MOD
                x = (x * x) % MOD
                p >>= 1
            return res
        
        MOD = 10**9 + 7
        countEven = (n + 1) // 2
        countOdd = n // 2

        combEven = power(5, countEven)
        combOdd = power(4, countOdd)
        return (combEven * combOdd) % MOD