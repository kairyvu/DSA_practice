class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counterS = Counter(s)

        for c in t:
            if c not in counterS or counterS[c] == 0:
                continue
            counterS[c] -= 1
        return sum(counterS.values())