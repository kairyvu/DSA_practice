class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif mid - 1 >= 0 and arr[mid] < arr[mid - 1]:
                r = mid - 1
            elif mid + 1 < len(arr) and arr[mid] < arr[mid + 1]: 
                l = mid + 1