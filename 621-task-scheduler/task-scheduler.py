class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n < 1:
            return len(tasks)
        hsmap = Counter(tasks)
        
        maxHeap = [-v for v in hsmap.values()]
        heapq.heapify(maxHeap)
        q = deque()
        res = 0

        while maxHeap or q:
            res += 1
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count != 0:
                    q.append((count, res + n))
            if q and q[0][1] == res:
                heapq.heappush(maxHeap, q.popleft()[0])
        return res