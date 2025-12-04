class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        n = len(s)
        cache = {}
        def backtrack(i):
            if i == n:
                return [""]
            if i in cache:
                return cache[i]
            res = []
            for j in range(i, n):
                w = s[i:j+1]
                if w not in wordDict:
                    continue
                stringList = backtrack(j + 1)
                if not stringList:
                    continue
                for string in stringList:
                    sentence = w
                    if string:
                        sentence += " " + string
                    res.append(sentence)
            cache[i] = res
            return res
        return backtrack(0)