class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                currString = ""
                repeatTime = ""
                while stack and stack[-1] != "[":
                    currString = stack.pop() + currString
                stack.pop()

                while stack and stack[-1].isdigit():
                    currDigit = stack.pop()
                    repeatTime = currDigit + repeatTime
                stack.append(currString * int(repeatTime))
        return "".join(stack)