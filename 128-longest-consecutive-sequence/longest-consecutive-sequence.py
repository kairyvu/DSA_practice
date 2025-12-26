class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if (num - 1) not in nums:
                curr = num
                currLength = 1
                while (curr + 1) in nums:
                    currLength += 1
                    curr += 1
                res = max(res, currLength)

        return res