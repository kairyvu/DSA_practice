class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        nums.sort()

        for i in range(n - 2):
            if nums[i] == 0:
                continue
            largestEdge = i + 2
            for j in range(i + 1, n - 1):
                while largestEdge < n and nums[i] + nums[j] > nums[largestEdge]:
                    largestEdge += 1
                res += largestEdge - j - 1
        return res