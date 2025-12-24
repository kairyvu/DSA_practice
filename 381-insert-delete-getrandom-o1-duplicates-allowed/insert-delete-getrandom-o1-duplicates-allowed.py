class RandomizedCollection:

    def __init__(self):
        self.numIndex = defaultdict(set)
        self.numList = []

    def insert(self, val: int) -> bool:
        self.numList.append(val)
        insertIndex = len(self.numList) - 1
        self.numIndex[val].add(insertIndex)
        if len(self.numIndex[val]) == 1:
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.numIndex or not self.numIndex[val]:
            return False
        
        valIndex = self.numIndex[val].pop()
        lastIndex = len(self.numList) - 1
        lastNum = self.numList[lastIndex]
        self.numList[valIndex] = lastNum
        if valIndex != lastIndex:
            self.numIndex[lastNum].remove(lastIndex)
            self.numIndex[lastNum].add(valIndex)
        self.numList.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.numList)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()