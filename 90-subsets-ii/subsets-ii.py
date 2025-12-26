class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        current = []
        def backtrack(start):
            res.append(current.copy())
            for i in range(start,len(nums)):
                if start < i and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i+1)
                current.pop()
        backtrack(0)
        return res