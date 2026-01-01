class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # (char, num of repetition)
        for c in s:
            if stack and stack[-1][0] == c:
                ch, rep = stack.pop()
                if rep + 1 < k:
                    stack.append((ch, rep + 1))
            else:
                stack.append((c, 1))
        
        res = []
        for c, rep in stack:
            res.append(c * rep)
        return "".join(res)