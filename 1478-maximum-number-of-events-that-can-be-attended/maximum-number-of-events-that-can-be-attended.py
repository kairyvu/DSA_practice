class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        minHeap = []
        currDay = 1
        n = len(events)
        i, res = 0, 0

        while i < n or minHeap:
            if not minHeap:
                currDay = events[i][0]
                heapq.heappush(minHeap, events[i][1])
                i += 1
            
            while i < n and currDay == events[i][0]:
                heapq.heappush(minHeap, events[i][1])
                i += 1
            
            while minHeap and minHeap[0] < currDay:
                heapq.heappop(minHeap)

            if minHeap:
                heapq.heappop(minHeap)
                res += 1
                currDay += 1
        return res