class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stopToBus = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stopToBus[stop].append(i)

        q = deque()
        visited = set()
        for bus in stopToBus[source]:
            q.append(bus)
            visited.add(bus)
        
        res = 1

        while q:
            for _ in range(len(q)):
                currBus = q.popleft()
                for stop in routes[currBus]:
                    if stop == target:
                        return res
                    for nextBus in stopToBus[stop]:
                        if nextBus in visited:
                            continue
                        visited.add(nextBus)
                        q.append(nextBus)
                    del stopToBus[stop]
            res += 1
        return -1