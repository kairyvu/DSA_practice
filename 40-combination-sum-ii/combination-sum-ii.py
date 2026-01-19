class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combination = []
        res = []
        n = len(candidates)

        def backtrack(startIndex, currTarget) -> bool:
            if currTarget == 0:
                res.append(combination.copy())
                return True
            
            for i in range(startIndex, n):
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > currTarget:
                    break
                combination.append(candidates[i])
                backtrack(i + 1, currTarget - candidates[i])
                combination.pop()
        backtrack(0, target)
        return res