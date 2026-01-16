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
                currHLength = 1
            maxHLength = max(maxHLength, currHLength)
        
        for i in range(len(vBars) - 1):
            if vBars[i] + 1 == vBars[i + 1]:
                currVLength += 1
            else:
                currVLength = 1
            maxVLength = max(maxVLength, currVLength)
        
        return (min(maxHLength, maxVLength) + 1) ** 2