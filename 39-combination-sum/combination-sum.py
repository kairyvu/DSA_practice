class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def backtrack(start,target,combination):
            if target==0:
                result.append(list(combination))
                return result
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                
                combination.append(candidates[i])
                backtrack(i,target-candidates[i],combination)
                combination.pop()
        candidates.sort()
        backtrack(0,target,[])
        return result
