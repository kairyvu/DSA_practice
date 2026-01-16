class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        maxHLength = maxVLength = 1
        currHLength = currVLength = 1
        for i in range(len(hBars) - 1):
            if hBars[i] + 1 == hBars[i + 1]:
                currHLength += 1
            else:
                maxHLength = max(maxHLength, currHLength)
                currHLength = 1
        maxHLength = max(maxHLength + 1, currHLength + 1)
        
        for i in range(len(vBars) - 1):
            if vBars[i] + 1 == vBars[i + 1]:
                currVLength += 1
            else:
                maxVLength = max(maxVLength, currVLength)
                currVLength = 1
        maxVLength = max(maxVLength + 1, currVLength + 1)
        
        return min(maxHLength, maxVLength) ** 2