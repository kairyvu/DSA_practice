class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hsmap = defaultdict(int)
        n = len(wall)

        for w in wall:
            currPos = 0
            for i in range(len(w) - 1):
                currPos += w[i]
                hsmap[currPos] += 1
        
        return n if not hsmap.values() else n - max(hsmap.values())