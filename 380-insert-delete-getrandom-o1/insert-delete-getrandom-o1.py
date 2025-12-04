class RandomizedSet:

    def __init__(self):
        self.hsmap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        if val in self.hsmap:
            return False
        self.hsmap[val] = len(self.numList)
        self.numList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hsmap:
            return False
        lastVal = self.numList[-1]
        removingIndex = self.hsmap[val]

        self.numList[removingIndex] = lastVal
        self.hsmap[lastVal] = removingIndex

        self.numList.pop()
        del self.hsmap[val]

        return True

    def getRandom(self) -> int:
        randIndex = randint(0, len(self.numList) - 1)
        return self.numList[randIndex]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()