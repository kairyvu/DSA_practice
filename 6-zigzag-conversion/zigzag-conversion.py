class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        currRow = 0
        nextRowMove = 1

        for c in s:
            res[currRow].append(c)
            if not 0 <= currRow + nextRowMove < numRows:
                nextRowMove *= -1
            currRow += nextRowMove

        return "".join("".join(row) for row in res)