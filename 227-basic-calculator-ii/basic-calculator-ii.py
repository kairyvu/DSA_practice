class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        lastNum, currNum = 0, 0
        sign = '+'

        for i, c in enumerate(s):
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            if (c in "+-*/" and c != " ") or i == len(s) - 1:
                if sign == "+" or sign == "-":
                    res += lastNum
                    lastNum = currNum if sign == "+" else -currNum
                elif sign == "*":
                    lastNum = lastNum * currNum
                elif sign == "/":
                    lastNum = int(lastNum / currNum)
                
                sign = c
                currNum = 0
        res += lastNum
        return res