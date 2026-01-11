class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def numOfSubarrays(target):
            if target < 0:
                return 0
            l = 0
            oddCount = 0
            res = 0

            for r in range(len(nums)):
                oddCount += (nums[r] % 2)
                while oddCount > target:
                    oddCount -= (nums[l] % 2)
                    l += 1
                res += (r - l + 1)
            return res

        return numOfSubarrays(k) - numOfSubarrays(k - 1)