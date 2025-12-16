class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)

        if n > rows * cols:
            return False
        visited = set()
        
        def dfs(r, c, i):
            if i == n:
                return True
            if not 0 <= r < rows or not 0 <= c < cols or board[r][c] != word[i] or (r, c) in visited:
                return False
            
            visited.add((r, c))
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            visited.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False