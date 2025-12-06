class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        hsmap = defaultdict(int)
        
        def computeStep(num):
            if num == 1:
                return 0
            if num in hsmap:
                return hsmap[num]
            hsmap[num] = 1 + computeStep(num // 2) if num % 2 == 0 else 1 + computeStep(3 * num + 1)
            return hsmap[num]
        
        computedArray = []
        for num in range(lo, hi + 1):
            computedArray.append((computeStep(num), num))
        computedArray.sort()
        
        return computedArray[k - 1][1]