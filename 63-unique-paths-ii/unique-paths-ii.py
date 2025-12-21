class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[0][0]:
            return 0
        m, n = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1
        memo = {}

        def dfs(r, c):
            if not (0 <= r <= m and 0 <= c <= n) or obstacleGrid[r][c] == 1:
                return 0
            if r == m and c == n:
                return 1
            if (r, c) in memo:
                return memo[(r, c)]
            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[(r, c)]
        
        return dfs(0, 0)