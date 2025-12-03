class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n

        while l < r:
            mid = (l + r) // 2
            left = float("-inf") if mid - 1 < 0 else nums[mid-1]
            right = float("-inf") if mid + 1 >= n else nums[mid+1]
            if nums[mid] > left and nums[mid] > right:
                return mid
            elif nums[mid] <= left:
                r = mid - 1
            elif nums[mid] <= right:
                l = mid + 1
        return l