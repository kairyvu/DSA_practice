class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hsmap = defaultdict(int)
        p1 = 0
        res = 0
        
        for p2 in range(len(fruits)):
            hsmap[fruits[p2]] += 1
            while len(hsmap) > 2:
                hsmap[fruits[p1]] -= 1
                if hsmap[fruits[p1]] == 0:
                    del hsmap[fruits[p1]]
                p1 += 1
            res = max(res, p2 - p1 + 1)
        return res