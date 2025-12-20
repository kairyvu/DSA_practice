class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counterS, counterT = Counter(s), Counter(t)

        res = 0
        for c in counterS:
            if c not in counterT:
                counterT[c] = 0
            diff = counterS[c] - counterT[c]
            if diff > 0:
                res += diff
        return res