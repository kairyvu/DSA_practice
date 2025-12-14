class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetChars, targetCount = defaultdict(int), len(t)

        for c in t:
            targetChars[c] += 1
        
        p1 = 0
        minLength = float("inf")
        res = [0, 0]
        for p2 in range(len(s)):
            currChar = s[p2]
            if currChar in targetChars:
                if targetChars[currChar] > 0:
                    targetCount -= 1
                targetChars[currChar] -= 1
            while targetCount == 0:
                if p2 - p1 + 1 < minLength:
                    minLength = p2 - p1 + 1
                    res = [p1, p2 + 1]
                leftChar = s[p1]
                if leftChar in targetChars:
                    if targetChars[leftChar] >= 0:
                        targetCount += 1
                    targetChars[leftChar] += 1
                p1 += 1
        
        l, r = res
        return s[l:r]