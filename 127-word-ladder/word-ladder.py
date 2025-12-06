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
            res += 1
            for _ in range(len(q)):
                currWord = q.popleft()
                for i in range(len(currWord)):
                    pattern = currWord[:i] + "*" + currWord[i+1:]
                    for w in patternDict[pattern]:
                        if w in visited:
                            continue
                        if w == endWord:
                            return res
                        visited.add(w)
                        q.append(w)
        return 0