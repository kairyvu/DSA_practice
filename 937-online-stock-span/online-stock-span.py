class StockSpanner:

    def __init__(self):
        self.stack = [] # (val, index)
        self.index = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        self.index += 1
        biggerIndex = 0 if not self.stack else self.stack[-1][1]
        self.stack.append((price, self.index))
        res = self.index - biggerIndex
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)