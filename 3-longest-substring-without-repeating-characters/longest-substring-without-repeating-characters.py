class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        existingChar = set()

        p1, res = 0, 0
        for p2 in range(len(s)):
            while s[p2] in existingChar:
                existingChar.remove(s[p1])
                p1 += 1
            existingChar.add(s[p2])
            res = max(res, p2 - p1 + 1)
        return res