class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hsmap = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c not in hsmap:
                stack.append(c)
                continue
            
            if not stack or stack[-1] != hsmap[c]:
                return False
            stack.pop()
        return True if not stack else False