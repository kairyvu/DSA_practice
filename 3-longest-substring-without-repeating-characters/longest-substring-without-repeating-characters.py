class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hsset = set()
        res = 0
        p1 = 0
        for p2 in range(len(s)):
            while s[p2] in hsset:
                hsset.remove(s[p1])
                p1 += 1

            res = max(res, p2 - p1 + 1)
            hsset.add(s[p2])
        return res