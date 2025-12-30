class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k])
        res = currSum

        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            res = max(res, currSum)
        return res / k