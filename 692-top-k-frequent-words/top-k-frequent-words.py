class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        maxHeap = []
        
        for w, count in counter.items():
            maxHeap.append((-count, w))
        
        heapq.heapify(maxHeap)
        res = []
        
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res