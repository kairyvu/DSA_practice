class MagicDictionary:

    def __init__(self):
        self.child = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            node = self.child
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['.'] = True


    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        
        def searchHelper(node, i, changed):
            if i == n:
                return changed and "." in node
            c = searchWord[i]

            for ch, nextCh in node.items():
                if ch == ".":
                    continue
                elif c == ch:
                    if searchHelper(nextCh, i + 1, changed):
                        return True
                else:
                    if not changed:
                        if searchHelper(nextCh, i + 1, True):
                            return True
            return False

        return searchHelper(self.child, 0, False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)