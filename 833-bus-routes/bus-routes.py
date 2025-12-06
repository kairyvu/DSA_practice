class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stopToBus = defaultdict(list)
        busToStop = defaultdict(set)

        for i, route in enumerate(routes):
            busToStop[i] = set(route)
            for stop in route:
                stopToBus[stop].append(i)

        q = deque([source])
        visitedBus = set()
        res = 0
        
        while q:
            res += 1
            n = len(q)
            for _ in range(n):
                currStop = q.popleft()
                nextBuses = stopToBus[currStop]
                for bus in nextBuses:
                    if bus in visitedBus:
                        continue
                    visitedBus.add(bus)
                    if target in busToStop[bus]:
                        return res
                    q.extend(busToStop[bus])
        return -1