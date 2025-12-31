class Pair:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    
    def __lt__(self, pair):
        return self.count < pair.count or (self.count == pair.count and self.word > pair.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        minHeap = []
        
        for w, count in counter.items():
            heapq.heappush(minHeap, Pair(w, count))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [p.word for p in sorted(minHeap, reverse=True)]