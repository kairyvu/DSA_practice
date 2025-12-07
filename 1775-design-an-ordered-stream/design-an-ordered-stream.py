class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * n
        self.index = 0
        self.cap = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        res = []
        while self.index < self.cap and self.stream[self.index] != "":
            res.append(self.stream[self.index])
            self.index += 1
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)