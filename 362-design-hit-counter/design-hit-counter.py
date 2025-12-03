from collections import deque, defaultdict
class HitCounter:
    def __init__(self):
        self.queue = deque()
        self.hsmap = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        if not self.queue or timestamp != self.queue[-1]:
            self.queue.append(timestamp)
        self.hsmap[timestamp] += 1
    
    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0] <= timestamp - 300:
            t = self.queue.popleft()
            del self.hsmap[t]
        return sum(x for x in self.hsmap.values())