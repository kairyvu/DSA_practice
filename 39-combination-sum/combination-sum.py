class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def backtrack(i, currComb, remaindingSum):
            if remaindingSum < 0 or i == n:
                return
            elif remaindingSum == 0:
                res.append(currComb.copy())
                return
            
            currComb.append(candidates[i])
            backtrack(i, currComb, remaindingSum - candidates[i])
            currComb.pop()
            backtrack(i + 1, currComb, remaindingSum)

        backtrack(0, [], target)
        return res