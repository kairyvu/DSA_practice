class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        visited = {}

        for i in range(len(nums)):
            if nums[i] in dups:
                continue
            dups.add(nums[i])
            for num in nums[i + 1:]:
                lastNum = -nums[i] - num
                if lastNum in visited and visited[lastNum] == i:
                    res.add(tuple(sorted([nums[i], num, lastNum])))
                visited[num] = i
        return [list(triplet) for triplet in res]