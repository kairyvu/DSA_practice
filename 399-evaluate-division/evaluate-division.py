class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            adj[eq[0]].append((eq[1], values[i]))
            adj[eq[1]].append((eq[0], 1 / values[i]))
        
        def bfs(start, target):
            if not (start in adj and target in adj):
                return -1
            
            q, visited = deque([(start, 1)]), set()
            while q:
                src, value = q.popleft()
                if src == target:
                    return value 
                
                visited.add(src)
                for dst, val in adj[src]:
                    if dst in visited:
                        continue
                    q.append((dst, value * val))
            return -1
        
        res = []
        for src, dst in queries:
            res.append(bfs(src, dst))
        return res