class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        occupied = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                occupied[r] |= 1 << c
        
        res = (n - len(occupied)) * 2
        
        LEFT = 1 << 2 | 1 << 3 | 1 << 4 | 1 << 5
        MID = 1 << 4 | 1 << 5 | 1 << 6 | 1 << 7
        RIGHT = 1 << 6 | 1 << 7 | 1 << 8 | 1 << 9

        for row in occupied.values():
            checkLeft = (row & LEFT) == 0
            checkRight = (row & RIGHT) == 0
            checkMid = (row & MID) == 0
            if checkLeft and checkRight:
                res += 2
            elif checkLeft or checkRight or checkMid:
                res += 1
        return res