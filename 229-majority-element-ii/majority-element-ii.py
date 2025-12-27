class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num1, num2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num1 == num:
                count1 += 1
            elif num2 == num:
                count2 += 1
            elif count1 == 0:
                num1 = num
                count1 = 1
            elif count2 == 0:
                num2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        if num1 is not None and nums.count(num1) > n // 3:
            res.append(num1)
        if num2 is not None and nums.count(num2) > n // 3:
            res.append(num2)
        return res