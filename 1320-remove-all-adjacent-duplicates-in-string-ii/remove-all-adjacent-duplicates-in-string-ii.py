class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1][0] == ch:
                char, time = stack.pop()
                time += 1
                if time < k:
                    stack.append((char, time))
            else:
                stack.append((ch, 1))

        res = []
        for ch, time in stack:
            res.append(ch * time)
        return "".join(res)