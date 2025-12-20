class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        q = deque([(0, 0)])
        res = 0
        n = len(grid)
        dirs = [[0, 1], [1, 1], [1, 0], [0, -1], [-1, 1], [-1, -1], [-1, 0], [1, -1]]
        while q:
            res += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return res
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if not (0 <= newR < n and 0 <= newC < n) or grid[newR][newC] == 1:
                        continue
                    grid[newR][newC] = 1
                    q.append((newR, newC))
        return -1