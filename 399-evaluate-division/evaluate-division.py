class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            adj[eq[0]].append((eq[1], values[i]))
            adj[eq[1]].append((eq[0], 1 / values[i]))
        
        def bfs(start, target):
            if not (start in adj and target in adj):
                return -1
            
            q, visited = deque([(start, 1)]), set([start])
            while q:
                node, value = q.popleft()
                if node == target:
                    return value 
                
                for nei, w in adj[node]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append((nei, value * w))
            return -1
        
        return [bfs(a, b) for a, b in queries]