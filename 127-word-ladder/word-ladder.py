class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        patternDict = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patternDict[pattern].append(word)
        
        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        res = 1
        
        while q:
            for _ in range(len(q)):
                currWord = q.popleft()
                if currWord == endWord:
                    return res
                for i in range(len(currWord)):
                    pattern = currWord[:i] + "*" + currWord[i+1:]
                    for w in patternDict[pattern]:
                        if w in visited:
                            continue
                        visited.add(w)
                        q.append(w)
            res += 1
        return 0