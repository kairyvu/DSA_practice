class Solution:
    def getBox(self, r, c):
        return 3 * (r // 3) + (c // 3)

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        digits = set("123456789")
        rows = [set() for _ in range(9)] 
        cols = [set() for _ in range(9)] 
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == ".":
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[self.getBox(r, c)].add(val)
        n = len(empties)

        def backtrack(i):
            if i == len(empties):
                return True
            
            bestCell = i
            bestCellValues = digits

            for index in range(i, n):
                r, c = empties[index]
                b = self.getBox(r, c)
                cellValues = digits - rows[r] - cols[c] - boxes[b]

                if not cellValues:
                    return False
                if len(cellValues) < len(bestCellValues):
                    bestCellValues = cellValues
                    bestCell = index
                    if len(bestCellValues) == 1:
                        break
            
            empties[i], empties[bestCell] = empties[bestCell], empties[i]
            r, c = empties[i]
            b = self.getBox(r, c)

            for val in bestCellValues:
                board[r][c] = val
                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)

                if backtrack(i + 1):
                    return True
                
                rows[r].remove(val)
                cols[c].remove(val)
                boxes[b].remove(val)
                board[r][c] = "."
            
            empties[i], empties[bestCell] = empties[bestCell], empties[i]
            return False
        
        backtrack(0)