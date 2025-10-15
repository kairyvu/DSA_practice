class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev, curr = 1, 1
        res = 0
        longest = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                res = max(res, min(prev, curr))
                longest = max(curr, longest)
                prev = curr
                curr = 1
                
        longestSplit = max(curr, longest) // 2
        res = max(res, min(prev, curr))
        return res if longestSplit < res else longestSplit