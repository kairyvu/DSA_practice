class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numOfFresh = 0
        q = deque()

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    numOfFresh += 1
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        res = 0
        while q and numOfFresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 1:
                        numOfFresh -= 1
                        grid[newR][newC] = 2
                        q.append((newR, newC))
            res += 1
        
        return res if numOfFresh == 0 else -1