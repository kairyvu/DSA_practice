class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []
        res = []
        n = len(candidates)
        def backtrack(index, currTarget):
            if index >= n or currTarget < 0:
                return
            elif currTarget == 0:
                res.append(combination.copy())
                return
            
            currCandidate = candidates[index]
            combination.append(currCandidate)
            backtrack(index, currTarget - currCandidate)
            combination.pop()
            backtrack(index + 1, currTarget)
        
        backtrack(0, target)
        return res
                