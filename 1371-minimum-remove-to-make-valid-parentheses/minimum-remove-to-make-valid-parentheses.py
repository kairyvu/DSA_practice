class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []

        for i in range(len(s)):
            if s[i] not in ["(", ")"]:
                res.append(s[i])
            elif s[i] == "(":
                stack.append(i)
                res.append("")
            else:
                if stack:
                    openIndex = stack.pop()
                    res.append(s[i])
                    res[openIndex] = "("
                else:
                    res.append("")
        return "".join(res)