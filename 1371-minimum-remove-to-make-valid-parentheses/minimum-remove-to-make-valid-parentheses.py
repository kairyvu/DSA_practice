class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stringList = list(s)
        stack = []

        for i, c in enumerate(stringList):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:
                    stringList[i] = ""
                    continue
                stack.pop()
        
        while stack:
            stringList[stack.pop()] = ""
        return "".join(stringList)