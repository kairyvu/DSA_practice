class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev, curr = 1, 1
        res = 0
        longest = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                res = max(res, min(prev, curr))
                longest = max(curr, longest)
                prev = curr
                curr = 1
                continue
            curr += 1
        longest = max(curr, longest)
        res = max(res, min(prev, curr))
        return res if longest // 2 < res else longest // 2