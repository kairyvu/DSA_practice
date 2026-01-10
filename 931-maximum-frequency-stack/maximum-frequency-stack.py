class FreqStack:

    def __init__(self):
        self.freqToVal = defaultdict(list)
        self.valToFreq = defaultdict(int)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.valToFreq[val] += 1
        self.freqToVal[self.valToFreq[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.valToFreq[val])

    def pop(self) -> int:
        num = self.freqToVal[self.maxFreq].pop()
        if len(self.freqToVal[self.maxFreq]) == 0:
            del self.freqToVal[self.maxFreq]
            self.maxFreq -= 1
        self.valToFreq[num] -= 1
        return num




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()