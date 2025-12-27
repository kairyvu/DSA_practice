class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        maxHeapLen, minHeapLen = len(self.maxHeap), len(self.minHeap)
        if maxHeapLen - minHeapLen > 1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        elif self.minHeap and self.maxHeap and self.minHeap[0] < -self.maxHeap[0]:
            maxHeapVal, minHeapVal = -heapq.heappop(self.maxHeap), heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -minHeapVal)
            heapq.heappush(self.minHeap, maxHeapVal)

    def findMedian(self) -> float:
        length = len(self.maxHeap) + len(self.minHeap)
        if length % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()