class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev1, prev2 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            currMax = max(nums[i] + prev1, prev2)
            prev1, prev2 = prev2, currMax
        return prev2