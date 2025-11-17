class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0
        i = 0
        while i < len(nums) and nums[i] != 1:
            i += 1
        
        i += 1
        while i < len(nums):
            if nums[i] == 0:
                count += 1
            else:
                if count < k:
                    return False
                count = 0
            i += 1
        return True