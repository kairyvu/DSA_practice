class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missingCount = 0

        for i, num in enumerate(arr):
            missingCount = num - (i + 1)
            if missingCount >= k:
                return num - (missingCount - k + 1)
        return arr[-1] + (k - missingCount)