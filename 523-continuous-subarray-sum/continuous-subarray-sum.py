class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = {0: -1}
        currSum = 0

        for i in range(len(nums)):
            currSum += nums[i]
            remainder = currSum % k
            if remainder in prefixSum:
                if i - prefixSum[remainder] >= 2:
                    return True
            else:
                prefixSum[remainder] = i
        return False