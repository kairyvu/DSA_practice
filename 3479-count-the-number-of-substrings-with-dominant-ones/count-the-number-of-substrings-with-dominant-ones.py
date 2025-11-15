class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        nextZero = [n] * n
        for i in range(n - 2, -1, -1):
            if s[i + 1] == "0":
                nextZero[i] = i + 1
            else:
                nextZero[i] = nextZero[i + 1]
        
        res = 0
        for l in range(n):
            zeroes = 1 if s[l] == "0" else 0
            r = l

            while zeroes * zeroes <= n:
                nextZ = nextZero[r]
                ones = (nextZ - l) - zeroes
                if ones >= zeroes * zeroes:
                    res += min(nextZ - r, ones - zeroes*zeroes + 1)
                r = nextZ
                zeroes += 1
                if r == n:
                    break
        return res