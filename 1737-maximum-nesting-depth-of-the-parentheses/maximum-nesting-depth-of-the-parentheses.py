class Solution:
    def maxDepth(self, s: str) -> int:
        currDepth, res = 0, 0
        for c in s:
            if c == "(":
                currDepth += 1
            elif c == ")":
                currDepth -= 1
            res = max(res, currDepth)
        return res