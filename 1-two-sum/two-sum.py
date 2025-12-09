class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsmap = {}
        
        for i, num in enumerate(nums):
            if target - num in hsmap:
                return [hsmap[target-num], i]
            hsmap[num] = i
        