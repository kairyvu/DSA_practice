class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, missing = -1, -1

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                dup = abs(num)
            else:
                nums[index] = -nums[index]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break
        return [dup, missing]