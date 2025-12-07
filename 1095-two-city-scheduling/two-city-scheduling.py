class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costDiff = []
        for costA, costB in costs:
            costDiff.append((costA - costB, costA, costB))
        costDiff.sort()
        res = 0
        
        half = len(costs) // 2
        for i in range(half):
            res += costDiff[i][1] + costDiff[i + half][2]
        return res
            