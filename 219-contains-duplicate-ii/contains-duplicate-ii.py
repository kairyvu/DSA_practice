class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hsmap = {}

        for i, num in enumerate(nums):
            if num in hsmap and i - hsmap[num] <= k:
                return True
            hsmap[num] = i
        return False