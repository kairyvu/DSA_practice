class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        def box_id(r, c):
            return (r // 3) * 3 + (c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empties.append((r, c))
                else:
                    v = board[r][c]
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[box_id(r, c)].add(v)

        def backtrack(i=0):
            if i == len(empties):
                return True

            r, c = empties[i]
            b = box_id(r, c)

            for v in "123456789":
                if v in rows[r] or v in cols[c] or v in boxes[b]:
                    continue

                board[r][c] = v
                rows[r].add(v)
                cols[c].add(v)
                boxes[b].add(v)

                if backtrack(i + 1):
                    return True

                rows[r].remove(v)
                cols[c].remove(v)
                boxes[b].remove(v)
                board[r][c] = "."

            return False

        backtrack()