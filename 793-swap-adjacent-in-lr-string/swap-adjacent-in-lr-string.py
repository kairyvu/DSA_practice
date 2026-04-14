class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        i, j = 0, 0
        n = len(start)
        
        while i < n or j < n:
            while i < n and start[i] == "X":
                i += 1
            while j < n and result[j] == "X":
                j += 1
            if i == n and j == n:
                break
            if i == n or j == n:
                return False
            if start[i] != result[j] or (start[i] == "L" and i < j) or (start[i] == "R" and i > j):
                return False
            i += 1
            j += 1
            
        return True