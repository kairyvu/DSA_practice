class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and stack[-1] > c and k > 0:
                stack.pop()
                k -= 1
            stack.append(c)
        
        res = stack[:-k] if k else stack
        return "".join(res).lstrip("0") or "0"